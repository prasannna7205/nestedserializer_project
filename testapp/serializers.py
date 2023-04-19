from testapp.models import Auther,Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class AutherSerializer(serializers.ModelSerializer):
    books_by_author = BookSerializer(read_only=True,many=True)
    class Meta:
        model=Auther
        fields='__all__'
