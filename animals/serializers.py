from rest_framework import serializers
from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Animal
        fields = "__all__"
