from django.db import models

class Tag(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

# Create your models here.
class Review(models.Model):
     """
     Model representing a review.
     """
     title = models.CharField(max_length=200)
     content = models.TextField()
     published_at = models.DateTimeField(auto_now_add=True)
     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     tags = models.ManyToManyField(Tag)

     def __str__(self):
         """
         String for representing the Model object.
         """
         return self.title




