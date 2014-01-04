#!/usr/bin/env python
# vim:fileencoding=utf-8
try:
    import autocomplete_light
    AUTOCOMPLETE_LIGHT_INSTALLED = True
except ImportError:
    AUTOCOMPLETE_LIGHT_INSTALLED = False

__author__ = 'zeus'

from django import forms
from models import Image, Album
from django.utils.translation import ugettext_lazy as _

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit, Button, Fieldset, HTML
from crispy_forms.bootstrap import InlineField, StrictButton

class ImageForm(forms.ModelForm):
    class Meta(object):
        model = Image
        exclude = ('user', 'order')

    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 19}), required=False,
                                  label=_('Description'))

    def __init__(self, user, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['album'].queryset = Album.objects.filter(user=user)
        self.fields['album'].required = True
        if AUTOCOMPLETE_LIGHT_INSTALLED:
            self.fields['tags'].widget = autocomplete_light.TextWidget('TagAutocomplete')
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-3 col-md-2'
        self.helper.field_class = 'col-sm-9 col-md-10'
        self.helper.form_action = 'imagestore:upload'
        self.helper.layout = Layout(
            'title',
            'description',
            'tags',
            'image',
            'album',
         Div(

                Submit('submit', 'Submit'),
                css_class='col-sm-offset-3 col-md-offset-2'
                )
            
            )




class AlbumForm(forms.ModelForm):
    class Meta(object):
        model = Album
        exclude = ('user', 'created', 'updated', 'order')


    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs and kwargs['instance']:
            self.fields['head'].queryset = Image.objects.filter(album=kwargs['instance'])
        else:
            self.fields['head'].widget = forms.HiddenInput()
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-inline'
        self.helper.form_show_labels = False
        self.helper.form_action = 'imagestore:create-album'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            InlineField('name'),
            Submit('submit', 'Submit')
            )




class ImageFormCrispy(forms.ModelForm):
    class Meta(object):
        model = Image
        exclude = ('user', 'order')


    def __init__(self, user, content_type=None, object_pk=None, *args, **kwargs):
        super(ImageFormCrispy, self).__init__(*args, **kwargs)
        self.fields['album'].queryset = Album.objects.filter(user=user)
        self.fields['album'].required = True
        if AUTOCOMPLETE_LIGHT_INSTALLED:
            self.fields['tags'].widget = autocomplete_light.TextWidget('TagAutocomplete')
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal upload-image'
        self.helper.form_action = 'imagestore:upload'
        self.helper.add_input(Submit('submit', 'Submit'))

