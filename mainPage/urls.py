from django.urls import re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^contacts/$', views.contacs, name='contacts'),

]