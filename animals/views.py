from rest_framework import viewsets, permissions
from .models import Animal
from .serializers import AnimalSerializer
from .permissions import IsOwnerOrReadOnly


class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = Animal.objects.all().order_by("-created_at")
        status = self.request.query_params.get("status")
        search = self.request.query_params.get("search")

        if status:
            queryset = queryset.filter(status=status)
        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset

    def perform_create(self, serializer):
        # ผูก owner อัตโนมัติจาก user ที่ล็อกอิน
        serializer.save(owner=self.request.user)
