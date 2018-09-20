from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^write/$', views.write, name='write'),
    url(r'^Korean/$', views.korean, name='korean'),
    url(r'^Mathematics/$', views.math, name='math'),
    url(r'^English/$', views.eng, name='english'),
    url(r'^PSO/$', views.pso, name='pso'),
#    url(r'^$', views.main_post, name='main_post'),
    url(r'^$', views.main_subject, name='main_subject'),
    url(r'^login/$', views.login, name='login'),
#    url(r'^look/$', views.look, name='look'),
    url(r'^look/(?P<post_id>\d+)/$', views.looks, name='looks'),
    url(r'^likes/(?P<post_id>\d+)/$', views.likes, name='likes'),
    url(r'^signup/$', views.signup, name='signup')
]
