from blogengine import views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stories', views.StoryViewSet)
router.register(r'users', views.UserViewSet)
