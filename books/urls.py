from django.urls import path
from .views import GenreListCreateView, GenreDetailView, BookListCreateView, BookDetailView

urlpatterns = [
    path("genres/", GenreListCreateView.as_view(), name="genre-list-create"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<slug:slug>/", BookDetailView.as_view(), name="book-detail"),
]