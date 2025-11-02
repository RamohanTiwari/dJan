from django.urls import path
from . import views

app_name = "playground"

# URLConf
urlpatterns = [
    path('hello/', views.say_hello, name='hello'),
    path('bye/', views.say_bye, name = 'bye'),
    path('contact/', views.contact, name='contact')
]
