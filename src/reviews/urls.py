from django.urls import path
from .views import (
    list_reviews,
    create_review,
    show_review,
    update_review,
    delete_review,
    media_autocomplete,
)

urlpatterns = [
    path("", list_reviews, name="list_reviews"),
    path("new", create_review, name="create_reviews"),
    path("<int:id>", show_review, name="show_review"),
    path("update/<int:id>/", update_review, name="update_review"),
    path("delete/<int:id>/", delete_review, name="delete_review"),
    path("media-autocomplete", media_autocomplete, name="media_autocomplete"),
]
