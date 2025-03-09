from django.urls import path
from . import views

urlpatterns= [
    path("events_list/", views.event_list, name='event-list'),
    path('create_event/', views.event_create, name='create-event'),
    path('update_event/<str:pk>/', views.update_event, name='update-event'),
    path('delete_event/<str:pk>/', views.delete_event, name='delete-event')
]