from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from imagestore.models import Album, Image
from imagestore.models import image_applabel, image_classname
from imagestore.models import album_applabel, album_classname
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from django.views import generic
from tagging.models import TaggedItem
from tagging.utils import get_tag
from django.db.models import Q

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
    username_field = User.USERNAME_FIELD
except ImportError:
    from django.contrib.auth.models import User
    username_field = 'username'


class IndexView(generic.ListView):
    context_object_name = 'image_list'
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
    	images = Image.objects.all()
    	tag_instance = get_tag('featured')
        if tag_instance is None:
            raise Http404(_('No Tag found matching "featured"'))
        images = TaggedItem.objects.get_by_model(images, tag_instance)
        return images

