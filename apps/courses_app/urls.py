from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    # url(r'^/new$', views.new),
    url(r'^create$', views.create),
    # url(r'^/(?P<id>\d+)$', views.show),
    # url(r'^/(?P<id>\d+)/edit$', views.edit),
    # url(r'^/update$', views.update),
    url(r'^courses/destroy/(?P<id>\d+)$', views.delete),
    url(r'^courses/destroy/(?P<id>\d+)/confirm_delete$', views.confirm_delete),

]