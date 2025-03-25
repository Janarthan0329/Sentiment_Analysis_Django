from django.db import models

# Create your models here.

class Review(models.Model):
    rating = models.IntegerField()
    date = models.DateField()
    variation = models.CharField(max_length=255)
    verified_review = models.TextField()
    feedback = models.IntegerField()

    def __str__(self):
        return f"Review {self.id} - Rating: {self.rating}"
