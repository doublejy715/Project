from django.urls import path
from . import views

 
urlpatterns = [
    path('',views.main),
    path('donga/', views.donga),
    path('hankookilbo/', views.hankookilbo),
    path('hankyung/', views.hankyung),
    path('khan/', views.khan),
    path('mk/', views.mk),
    path('seoul/', views.seoul),

]
