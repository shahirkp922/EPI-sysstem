from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('',views.index,name='index'),
    path('profile/', views.profile_view, name='profile'),
    path('about/',views.about,name='about'),
    path('refar/',views.refar,name='refar'),
    path('terms/',views.terms,name='terms'),
    path('contact/',views.contact,name='contact'),
    path('privacy/',views.privacy,name='privacy'),
    path('logout/', views.logout_view, name='logout'),
    
    
]