from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'testWB/$', views.index, name= 'testWB'),
    url(r'404_error/$', views._404, name= '404'),
    url(r'blank_/$', views.blank, name= 'blank'),
    url(r'buttons_/$', views.buttons, name= 'buttons'),
    url(r'cards/$', views.cards, name= 'cards'),
    url(r'utilities_color/$', views.utilities_color, name= 'utilities_color'),
    url(r'utilities_border/$', views.utilities_border, name= 'utilities_border'),
    url(r'utilities_animation/$', views.utilities_animation, name= 'utilities_animation'),
    url(r'utilities_other/$', views.utilities_other, name= 'utilities_other'),
    url(r'login/$', views.login, name= 'login'),
    url(r'register/$', views.register, name= 'register'),
    url(r'forgot_password/$', views.forgot_password, name= 'forgot_password'),
    url(r'charts/$', views.charts, name= 'charts'),
    url(r'tables/$', views.tables, name= 'tables'),
    url(r'logout/$', views.logout ,name= 'logout'),

    url(r'test/$', views.test, name= 'test'),
]
