from rest_framework import serializers
from .models import Book, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name", "description", "slug"]
        read_only_fields = ["id", "slug"]

class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)
    genre_id = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), source="genre", write_only=True
    )

    class Meta:
        model = Book
        fields = ["id", "title", "author", "genre", "genre_id", "synopsis", "cover_image", "published_date", "slug", "rating_average"]
        read_only_fields = ["id", "slug", "rating_average"]