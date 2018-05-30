"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from post import views as post_views
from user import views as user_views


urlpatterns = [
    url('^$', post_views.post_list),
    url('^create',post_views.create),
    url('^edit', post_views.edit),
    url('^read',post_views.read),
    url('^search',post_views.search),
    url('^comment',post_views.comment),
    url('^top10',post_views.top10),

    url('^register',user_views.register),
    url('^login',user_views.login),
    url('^logout',user_views.logout),
    url('^user_info',user_views.user_info),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)