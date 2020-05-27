from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serialize name."""

    name = serializers.CharField(max_length=200)
    