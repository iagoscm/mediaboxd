from django.shortcuts import render
from reviews.models import Media


def index(request):
    movie = Media.objects.filter(media_type="movie").values(
        "cover_url", "id", "media_type", "name"
    ).first()
    book = Media.objects.filter(media_type="book").values(
        "cover_url", "id", "media_type", "name"
    ).first()
    game = Media.objects.filter(media_type="game").values(
        "cover_url", "id", "media_type", "name"
    ).first()
    serie = Media.objects.filter(media_type="serie").values(
        "cover_url", "id", "media_type", "name"
    ).first()

    print({"movie": movie, "book": book, "game": game, "serie": serie})
    print(movie)
    return render(
        request,
        "index.html",
        {"movie": movie, "book": book, "game": game, "serie": serie},
    )
