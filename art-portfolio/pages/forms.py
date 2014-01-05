__author__ = 'goldhand'

from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit, Button, Fieldset, HTML
from crispy_forms.bootstrap import InlineField, StrictButton

class FeedbackForm(forms.Form):
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	subject = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
	feedback = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message...'}))
	next = forms.HiddenInput()
	
	def __init__(self, *args, **kwargs):
		super(FeedbackForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = True
		self.helper.form_class = ''
		self.helper.form_show_labels = False
		self.helper.form_action = 'pages:feedback'
		self.helper.layout = Layout(
            'email',
            'subject',
            'feedback',
            'next',
         	Div(
            	Submit('submit', 'Send'),
                css_class='center-div'
            )
        )