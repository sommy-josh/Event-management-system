from django.urls import path
from . import views

urlpatterns =[
    path("booking_list/", views.booking_list, name="booking-list"),
    path('book_create/', views.booking_create,name="book-create"),
]