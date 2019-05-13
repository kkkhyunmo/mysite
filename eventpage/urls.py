from django.urls import path
from . import views

urlpatterns = [
    path('lavinia-event-arajji/', views.laviniaA, name='laviniaA'),
    path('lavinia-event-arajji/<webtoon>', views.laviniaA_false, name='laviniaA_false'),
    path('lavinia-event-arajji-success/', views.laviniaA_success, name='laviniaA_success'),
    path('lavinia-event-normal/', views.laviniaN, name='laviniaN'),
    path('lavinia-event-normal/<webtoon>', views.laviniaN_false, name='laviniaN_false'),
    path('lavinia-event-normal-success/', views.laviniaN_success, name='laviniaN_success'),
    path('rainbowhouse-event-arajji/', views.rainbowhouseA, name='rainbowhouseA'),
    path('rainbowhouse-event-arajji/<webtoon>', views.rainbowhouseA_false, name='rainbowhouseA_false'),
    path('rainbowhouse-event-arajji-success/', views.rainbowhouseA_success, name='rainbowhouseA_success'),
    path('rainbowhouse-event-normal/', views.rainbowhouseN, name='rainbowhouseN'),
    path('rainbowhouse-event-normal/<webtoon>', views.rainbowhouseN_false, name='rainbowhouseN_false'),
    path('rainbowhouse-event-normal-success/', views.rainbowhouseN_success, name='rainbowhouseN_success'),
]