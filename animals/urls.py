from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import AnimalViewSet, CurrentUserView

router = DefaultRouter()
router.register(r"animals", AnimalViewSet, basename="animals")

urlpatterns = [
    *router.urls,
    path("users/me/", CurrentUserView.as_view()),
]
