from django.db import models
from books.models import Book
from users.models import User

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recommendations")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="recommendations")
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} recommends {self.book.title}"