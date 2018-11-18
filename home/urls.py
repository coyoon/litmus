from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^library$', views.library, name='library'),
    url(r'^about$', views.about, name='about'),
]
