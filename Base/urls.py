from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),            # root page → home.html
    path('about/', views.about, name='about'),    # /about/ → about.html
    path('projects/', views.projects, name='projects'),
     path('skills/', views.skills, name='skills'),# /projects/ → projects.html
    path('contact/', views.contact, name='contact'),     # POST target for form
]
