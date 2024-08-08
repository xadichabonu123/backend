from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, UserResponseViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'responses', UserResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
