from booking.views import  search_rooms, register_invoice, get_invoice, get_booking
from django.urls import path 

urls =[
    
    path('api/booking/search_rooms/<str:start_date>/<str:end_date>/<int:guests>', search_rooms, name="search-rooms"),
    path('api/booking/<int:booking_id>/', get_booking, name="get_booking"),
    path('api/invoice/', register_invoice, name="register_invoice"),
    path('api/invoice/<int:invoice_id>/', get_invoice, name="get_invoice"),
]

