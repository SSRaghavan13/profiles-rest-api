from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from . import serializers
from . import models
from . import permissions

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

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello msg."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partical_update)',
            'Auto mapping URLs uing routers',
            'More func with less code'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create new hello message."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Updates an object."""

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Updates part of an object."""

        return Response({'http_method':'PATCH'})
    
    def destroy(self, request, pk=None):
        """Deletes an object."""

        return Response({'http_method':'Delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations on profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # Creating a tuple to make it immutable
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)