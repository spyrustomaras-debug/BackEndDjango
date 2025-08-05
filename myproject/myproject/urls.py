from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'useraccounts', views.UserAccountViewSet)
router.register(r'authors', views.AuthorViewSet, basename='author')
router.register(r'books', views.BookViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'courses', views.CourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
