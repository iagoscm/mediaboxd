from django.test import TestCase
from .models import Review, Media
from django.contrib.auth.models import User

class ReviewTestCase(TestCase):
    def setUp(self):
        self.author = User.objects.create(username='testuser', password='12345')
        self.media = Media.objects.create(
            cover_url="https://i.imgur.com/Zvb1d0t.jpeg",
            name="The Matrix",
            description="A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
            release_date="1999-03-31",
            media_type="movie",
        )

    def test_reviews_can_created(self):
        title = 'Test Review'
        content = 'This is a test review'
        review = Review.objects.create(
            title=title,
            content=content,
            author=self.author,
            media=self.media,
        )

        review_encontrada = Review.objects.get(id=review.id)
        self.assertEqual(review_encontrada.title, title)
