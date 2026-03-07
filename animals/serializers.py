from rest_framework import serializers
from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    # รับไฟล์จาก form-data key = "image"
    image = serializers.ImageField(write_only=True, required=False)

    # ไม่ให้แก้ owner เอง
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Animal
        fields = "__all__"
        read_only_fields = ("image_url", "image_public_id", "owner")

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name is required")

        if len(value) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters")

        return value
