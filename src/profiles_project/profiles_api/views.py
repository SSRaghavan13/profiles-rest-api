from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

class HelloAPIView(APIView):
    """Testing."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'HTTP methods (get, post, patch, put, delete)',
            'Similar to traditional django view',
            'Most control',
            'Mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create hello msg with name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields in request."""

        return Response({'method': 'patch'})
    
    def delete(self, request, pk=None):
        """Delete object."""

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API viewset."""

    def list(self, request):
        """Return a hello msg."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partical_update)',
            'Auto mapping URLs uing routers',
            'More func with less code'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})