from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Profile, UserAccount, Author, Book, Student, Course
from .serializers import (ProfileSerializer, UserAccountSerializer,
                          AuthorSerializer, BookSerializer,
                          StudentSerializer, CourseSerializer)

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer
from .services.author_service import AuthorService
from .repositories.author_repository import AuthorRepository
from django.db.models.fields.related import ManyToManyField, ForeignKey

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserAccountViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = AuthorService(AuthorRepository())

    def get_queryset(self):
        # Return all authors (QuerySet or list)
        return self.service.list_authors()

    def list(self, request, *args, **kwargs):
        authors = self.get_queryset()
        serializer = self.get_serializer(authors, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None, *args, **kwargs):
        author = self.service.get_author(int(pk))
        if not author:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(author)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        name = request.data.get("name")
        if not name:
            return Response({"detail": "Name is required"}, status=status.HTTP_400_BAD_REQUEST)
        author = self.service.create_author(name)
        serializer = self.get_serializer(author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, *args, **kwargs):
        # pk is the author's ID
        updated_author = self.service.update_author(int(pk), **request.data)
        if not updated_author:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(updated_author)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None, *args, **kwargs):
        success = self.service.delete_author(int(pk))
        if not success:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # other methods unchanged


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
