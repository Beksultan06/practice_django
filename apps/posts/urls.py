from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog_single/', views.blog, name='blog_single'),
    path('portfolio/<int:id>/', views.image, name='image'),
]