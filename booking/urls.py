from booking.views import hello_word
from django.urls import path 

urls =[
    path('api/hello-word', hello_word, name="hello-word")
]

