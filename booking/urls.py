from booking.views import hello_word, search_rooms
from django.urls import path 

urls =[
    path('api/hello-word', hello_word, name="hello-word"),
    path('api/booking/search_rooms/<str:start_date>/<str:end_date>/<int:guests>', search_rooms, name="search-rooms"),
]

