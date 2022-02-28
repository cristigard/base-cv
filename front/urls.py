from django.urls import path
from . import views 



urlpatterns = [
    
    path('', views.home, name = 'home'),
    path('<str:tk>/', views.cv, name = 'cv'),
    path('update/skill', views.skills, name = 'skills'),
    path('update/language', views.language, name = 'languages'),
    path('update/about', views.about, name = 'about'),
    path('update/work', views.work, name = 'works'),
    path('update/education', views.education, name = 'education'),
    path('update/objective', views.objective, name = 'objective'),
    ]