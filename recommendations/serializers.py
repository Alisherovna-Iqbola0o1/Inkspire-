from rest_framework import serializers
from .models import Recommendation

class RecommendationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    book = serializers.StringRelatedField()

    class Meta:
        model = Recommendation
        fields = ["id", "user", "book", "comment", "created_at"]
        read_only_fields = ["id", "created_at", "user"]