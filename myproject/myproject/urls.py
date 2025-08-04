from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp import views

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'useraccounts', views.UserAccountViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'courses', views.CourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
