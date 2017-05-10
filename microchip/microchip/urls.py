"""microchip URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
import blog.views as views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get_posts/', views.get_posts),
    url(r'^login/', views.authenticate),
    url(r'^logout/', views.logout),
    url(r'^add_post/', views.add_post),
    url(r'^delete_post/', views.delete_post),
    url(r'^edit_post/', views.edit_post),
    url(r'^get_comments_for_post/', views.get_comments_for_post),
    url(r'^logged_in/', views.logged_in),
    url(r'^delete_comment/', views.delete_comment),
    url('^upload_image/', views.upload_image),
    url('^get_images/', views.get_images),
    url('^delete_image/', views.delete_image),
    url('^edit_contact_info/', views.edit_contact_info),
    url('^is_contact_filled/', views.is_contact_filled),
    url('^create_contact/', views.create_contact),
    url('^get_contact_info/', views.get_contact_info),
    url('^get_post/', views.get_post),
    url('^post/(.*)', views.show_post),
    url(r'^$', views.index),
]
