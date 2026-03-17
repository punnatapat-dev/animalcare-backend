from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
import cloudinary.uploader

from .models import Animal
from .serializers import AnimalSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response


class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        queryset = Animal.objects.all().order_by("-created_at")
        status = self.request.query_params.get("status")
        search = self.request.query_params.get("search")
        species = self.request.query_params.get("species")

        if species:
            queryset = queryset.filter(species=species)

        if status:
            queryset = queryset.filter(status=status)
        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset

    @action(detail=False, methods=["get"], url_path="stats")
    def stats(self, request):
        total = Animal.objects.count()
        available = Animal.objects.filter(status="AVAILABLE").count()
        adopted = Animal.objects.filter(status="ADOPTED").count()
        pending = Animal.objects.filter(status="PENDING").count()

        dogs = Animal.objects.filter(species="DOG").count()
        cats = Animal.objects.filter(species="CAT").count()
        rabbits = Animal.objects.filter(species="RABBIT").count()
        other = Animal.objects.filter(species="OTHER").count()

        return Response(
            {
                "total": total,
                "available": available,
                "adopted": adopted,
                "pending": pending,
                "dogs": dogs,
                "cats": cats,
                "rabbits": rabbits,
                "other": other,
            }
        )

    def perform_create(self, serializer):
        image_file = serializer.validated_data.pop("image", None)

        animal = serializer.save(owner=self.request.user)

        if image_file:
            result = cloudinary.uploader.upload(
                image_file,
                folder="animalcare/animals",
                resource_type="image",
            )
            animal.image_url = result["secure_url"]
            animal.image_public_id = result["public_id"]
            animal.save(update_fields=["image_url", "image_public_id"])

    def perform_update(self, serializer):
        image_file = serializer.validated_data.pop("image", None)

        animal = serializer.save()

        if image_file:
            if animal.image_public_id:
                cloudinary.uploader.destroy(
                    animal.image_public_id, resource_type="image"
                )

            result = cloudinary.uploader.upload(
                image_file,
                folder="animalcare/animals",
                resource_type="image",
            )
            animal.image_url = result["secure_url"]
            animal.image_public_id = result["public_id"]
            animal.save(update_fields=["image_url", "image_public_id"])
