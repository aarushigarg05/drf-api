from django.contrib import admin
from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)
# no base name here because we have a query set and drf will figure it out khud se
# if we want to over ride it then we can specify it
urlpatterns = [
    path('hello-api/',views.HelloView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls)),
]
