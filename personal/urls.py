from django.urls import path
from .import views

urlpatterns = [
    path ('about_me/', views.about_me,
          name = 'about_me'),
    path('index/',views.index,
         name = 'index'),
    path('installing_bootstrap/',views.installing_bootstrap,
         name = 'installing_bootstrap'),
]

