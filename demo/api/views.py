from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import *
from .models import * 
from rest_framework import status
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class UserList(APIView):
    """
    List all Users, or create a new User object.
    """
    #permission_classes = [IsAllowedToWrite]
    def get(self, request, format=None):
        query  = request.query_params.get('name')
        if query  is None:
            query = ""
        sort = request.query_params.get("sort")
        if sort == None:
            task = Users.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query))
        else:
            task = Users.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query)).order_by(sort)
        page = request.query_params.get("page")
        limit = request.query_params.get("limit")
        if limit == None:
            limit = 5
        paginator = Paginator(task, limit)
        try:
            task = paginator.page(page)
        except PageNotAnInteger:
            task = paginator.page(1)        
        serializer = UserSerializer(task, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       
            
        return Response()

class UserDetail(APIView):
    """
    Retrieve, update or delete a User instance.
    """
    
    def get_object(self, id):
        try:
            return Users.objects.get(id=id)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        task = self.get_object(id)
        serializer = UserSerializer(task)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        task = self.get_object(id)
        serializer = UserSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        task = self.get_object(id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
