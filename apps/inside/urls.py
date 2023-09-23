from django.urls import path
from . import views

urlpatterns = [
    path('inside/<int:id>/', views.Inside, name='inside'),

]
