from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET']) 
def hello_word(request):
    return Response({"message":"hello"})

@api_view(['GET'])
def search_rooms(request, start_date, end_date, guests):
    
    return Response({"response":""} )