
from django.urls import path, include # type: ignore
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.home, name='home'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('more', views.more, name='more'),
    path('aboutus', views.aboutus, name='aboutus'),

]
