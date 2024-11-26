from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<int:pk>/', views.event_details, name='event_details'),  # Ensure the URL pattern matches the view function name
]