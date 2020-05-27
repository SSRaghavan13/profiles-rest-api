from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Testing."""

    def get(self, request, format=None):
        an_apiview = [
            'HTTP methods (get, post, patch, put, delete)',
            'Similar to traditional django view',
            'Most control',
            'Mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})