from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'pypi/(?P<package>[\w\-_]+)/', views.pingback, name='pypi', kwargs={'repository': 'pypi'}),
]
