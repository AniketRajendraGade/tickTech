
from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.user_register),
    path('dashboard',views.dashboard),
    path('register',views.user_register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
    path('catfilter/<cv>',views.catfilter),
    path('statfilter/<sf>',views.statfilter),
    path('datefilter',views.datefilter),
    path('datesort/<dv>',views.datesort),
]