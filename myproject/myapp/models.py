# Create your models here.
from django.db import models

# One-to-One relationship
class Profile(models.Model):
    user_name = models.CharField(max_length=100)
    bio = models.TextField()
    
class UserAccount(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='account')
    email = models.EmailField()

# One-to-Many relationship
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=200)
    
# Many-to-Many relationship
class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, related_name='courses')
