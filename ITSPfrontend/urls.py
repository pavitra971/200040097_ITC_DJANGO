from django.contrib import admin
from django.urls import path
from ITSPfrontend import views

urlpatterns = [
    
    path("", views.index,name='ITSPfrontend'),
    path("SumSquad", views.SumSquad,name='SumSquad'),
    path("ITS21001", views.ITS21001,name='ITS21001'),
    path("ITS21002", views.ITS21002,name='ITS21002'),
    path("ITS21003", views.ITS21003,name='ITS21003'),
    path("ITS21004", views.ITS21004,name='ITS21004'),
    path("ITS21005", views.ITS21005,name='ITS21005'),
    path("ITS21006", views.ITS21006,name='ITS21006'),
    path("ITS21007", views.ITS21007,name='ITS21007'),
    path("ITS21008", views.ITS21008,name='ITS21008'),
    path("ITS21009", views.ITS21009,name='ITS21009'),
    path("ITS21010", views.ITS21010,name='ITS21010'),

    path("ITS31001", views.ITS31001,name='ITS31001'),
    path("ITS31002", views.ITS31002,name='ITS31002'),
    path("info", views.info,name='info'),
    path('Info/', views.Info_list),
    path('Info/<int:pk>/', views.Info_detail),    
]
