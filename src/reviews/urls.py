
from django.urls import path
from .views import list_reviews, create_review, update_review, delete_review

urlpatterns = [
    path('', list_reviews, name='list_reviews'),
    path('new', create_review, name='create_reviews'),
    path('update/<int:id>/', update_review, name='update_review'),
    path('delete/<int:id>/', delete_review, name='delete_review'),
]
