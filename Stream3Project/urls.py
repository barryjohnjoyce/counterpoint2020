"""Stream3Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles import views as static_views
from homeApp import views as homeApp_views
from accountsApp import views as accountsApp_views
from .settings import MEDIA_ROOT
from django.views.static import serve
from threadsApp import views as forum_views
import threadsApp


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homeApp_views.get_index, name='index'),

    url(r'^about/$', homeApp_views.get_about, name='about'),
    url(r'^contact/$', homeApp_views.get_contact, name='contact'),

    url(r'^register/$', accountsApp_views.register, name='register'),
    url(r'^profile/$', accountsApp_views.profile, name='profile'),
    url(r'^login/$', accountsApp_views.login, name='login'),
    url(r'^logout/$', accountsApp_views.logout, name='logout'),

    #static view
    url(r'^static/(?P<path>.*)$', static_views.serve),

    url(r'', include('blogApp.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^cancel_subscription/$', accountsApp_views.cancel_subscription, name='cancel_subscription'),
    url(r'^cancellation/$', accountsApp_views.cancellation, name='cancellation'),

    # Forum Views
    url(r'^forum/$', forum_views.forum, name='forum'),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$',  threadsApp.views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', forum_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', forum_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$',forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<post_id>\d+)/$', forum_views.delete_post, name='delete_post'),

    # Poll Views
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', forum_views.thread_vote, name='cast_vote'),
]
