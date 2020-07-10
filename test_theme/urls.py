from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^testWB/$', views.test, name= 'testWB'),
]
