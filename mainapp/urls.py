from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('home/', views.home),
    path('about/', views.about),
    path('proinfo/', views.proinfo),
    path('showcase/', views.showcase),
    path('survey/', views.survey),
    path('contact/', views.contact),
    path('snippet', views.snippet_detail)
]