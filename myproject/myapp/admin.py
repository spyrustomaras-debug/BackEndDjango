from django.contrib import admin
from .models import (
    Profile,
    UserAccount,
    Author,
    Book,
    Student,
    Course
)

# Register each model
admin.site.register(Profile)
admin.site.register(UserAccount)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Course)
