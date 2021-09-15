from django.db import models

# Create your models here.
class Review(models.Model):
     """
     Model representing a review.
     """
     title = models.CharField(max_length=200)
     content = models.TextField()
     date_published = models.DateTimeField(auto_now_add=True)
     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

     def __str__(self):
         """
         String for representing the Model object.
         """
         return self.title