from django.urls import path
from . import views

app_name = 'app_folder'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('time_line/', views.time_line, name='time_line'),
    path('history/', views.history, name='history'),
    path('registed/', views.registed, name='registed'),
    path('saved/', views.saved, name='saved'),
    path('notlogin/', views.notlogin, name='notlogin'),
    path('registed/login/', views.registed_login, name='registed_login'),
    path('registed/personal/', views.registed_personal, name='registed_personal'),
    path('registed/login/terms/', views.registed_login_terms, name='registed_login_terms'),
    path('registed/login/login/', views.registed_login_login, name='registed_login_login'),
    path('registed/login/create/', views.registed_login_create, name='registed_login_personal'),
    path('logout/', views.logout, name='logout'),
    path('admin/', views.sample, name='admin'),
]