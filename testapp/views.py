from django.shortcuts import render
from testapp.models import Auther,Book
from testapp.serializers import AutherSerializer,BookSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.
class AutherListView(ListCreateAPIView):
    queryset = Auther.objects.all()
    serializer_class=AutherSerializer

class AutherView(RetrieveUpdateDestroyAPIView):
    queryset = Auther.objects.all()
    serializer_class=AutherSerializer

class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class=BookSerializer

class BookView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class=BookSerializer
