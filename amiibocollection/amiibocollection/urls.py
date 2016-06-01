"""amiibocollection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import amiibo.views

urlpatterns = [
    url(r'^$', amiibo.views.ListAmiiboView.as_view(),
        name='amiibo-list'),
    url(r'^new$', amiibo.views.CreateAmiiboView.as_view(),
        name='amiibo-new',),
    url(r'^delete/(?P<pk>\d+)/$', amiibo.views.DeleteAmiiboView.as_view(),
        name='amiibo-delete',),
    url(r'^edit/(?P<pk>\d+)/$', amiibo.views.UpdateAmiiboView.as_view(),
        name='amiibo-edit',),
    url(r'^(?P<pk>\d+)/$', amiibo.views.AmiiboView.as_view(),
        name='amiibo-view',),
    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page': 'django.contrib.auth.views.login'}),
    url(r'^register/$',amiibo.views.AmiiboRegister.as_view(),
            name='amiibo-register'),
    url(r'^admin/', admin.site.urls),
]


urlpatterns += staticfiles_urlpatterns()
