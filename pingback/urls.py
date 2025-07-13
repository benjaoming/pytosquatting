from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'pypi/(?P<package>[\w\-_]+)/', views.pingback, name='pypi', kwargs={'repository': 'pypi'}),
]
