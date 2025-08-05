from rest_framework import serializers
from .models import Profile, UserAccount, Author, Book, Student, Course

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserAccountSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserAccount
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, required=False)  # Nested field

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    def create(self, validated_data):
        books_data = validated_data.pop('books', [])
        author = Author.objects.create(**validated_data)

        for book_data in books_data:
            Book.objects.create(author=author, **book_data)

        return author
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
