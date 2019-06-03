from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('lavinia-event-arajji/', views.laviniaA, name='laviniaA'),
    path('lavinia-event-arajji-success/', views.laviniaA_success, name='laviniaA_success'),
    path('lavinia-event-normal/', views.laviniaN, name='laviniaN'),
    path('lavinia-event-normal-success/', views.laviniaN_success, name='laviniaN_success'),
    path('rainbowhouse-event-arajji/', views.rainbowhouseA, name='rainbowhouseA'),
    path('rainbowhouse-event-arajji-success/', views.rainbowhouseA_success, name='rainbowhouseA_success'),
    path('rainbowhouse-event-normal/', views.rainbowhouseN, name='rainbowhouseN'),
    path('rainbowhouse-event-normal-success/', views.rainbowhouseN_success, name='rainbowhouseN_success'),
]