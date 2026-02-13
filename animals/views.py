# animals/views.py
from rest_framework import viewsets, permissions
from .models import Animal  # <--- เพิ่มบรรทัดนี้!!!
from .serializers import AnimalSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all().order_by("-created_at")
    serializer_class = AnimalSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]  # แนะนำตัวนี้ถ้าจะเอา "อ่านได้แต่ห้ามแก้"
