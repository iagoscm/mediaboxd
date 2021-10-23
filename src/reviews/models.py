from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Media(models.Model):

    class MediaType(models.TextChoices):
        BOOK = 'book'
        MOVIE = 'movie'
        MUSIC = 'music'
        GAME = 'game'
        OTHER = 'other'

    cover_url = models.TextField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    media_type = models.CharField(
        max_length=10,
        choices=MediaType.choices,
        default=MediaType.OTHER
    )

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class Tag(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

# Create your models here.
class Review(models.Model):
     """
     Model representing a review.
     """
     RATING_CHOICES = (
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10'),
        )
    

     title = models.CharField(max_length=200)
     content = models.TextField()
     published_at = models.DateTimeField(auto_now_add=True)
     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     tags = models.ManyToManyField(Tag)
     rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=0,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
     media = models.ForeignKey(Media, on_delete=models.CASCADE)

     def __str__(self):
         return self.title
     media = models.ForeignKey(Media, on_delete=models.CASCADE, null=True)


     def __str__(self):
         """
         String for representing the Model object.
         """
         return self.title