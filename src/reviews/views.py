from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Media
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

def list_reviews(request):
    query = request.GET.get("q")
    media_type = request.GET.get("media_type")

    if request.GET.get("q"):
        query = request.GET.get("q")
        reviews = Review.objects.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(media__name__icontains=query)
            | Q(media__media_type__icontains=query)
            | Q(tags__title__icontains=query)
        )
    if request.GET.get("media_type"):
        query = request.GET.get("media_type")
        reviews = Review.objects.filter(media__media_type__icontains=query)
    if request.GET.get("u"):
        query = request.GET.get("u")
        reviews = Review.objects.filter(author__username__icontains=query)
    else:
        reviews = Review.objects.all()

    return render(request, "reviews/list-public.html", {"reviews": reviews, "query": query})


@login_required
def list_reviews_me(request):
    query = request.GET.get("q")

    if query:
        reviews = Review.objects.filter(
            (Q(title__icontains=query) | Q(content__icontains=query))
            & (Q(author_id__exact=request.user.id))
        )
    else:
        reviews = Review.objects.filter(Q(author_id__exact=request.user.id))

    return render(request, "reviews/list-me.html", {"reviews": reviews})


@login_required
def create_review(request):
    form = ReviewForm(request.POST or None)

    if form.is_valid():
        review = form.save(commit=False)
        review.author = request.user
        review.media = Media.objects.get(pk=form.cleaned_data["media_id"])
        review.save()
        return redirect("list_reviews_me")

    return render(request, "reviews/form-create.html", {"form": form})


@login_required
def update_review(request, id):
    review = Review.objects.get(id=id)
    form = ReviewForm(request.POST or None, instance=review, initial={"media_id": review.media.id, "media_value": review.media.name})

    if form.is_valid():
        review = form.save(commit=False)
        review.media = Media.objects.get(pk=form.cleaned_data["media_id"])
        review.save()
        return redirect("list_reviews_me")

    return render(request, "reviews/form-update.html", {"form": form, "review": review})


@login_required
def delete_review(request, id):
    task = get_object_or_404(Review, pk=id)
    task.delete()

    messages.info(request, "Tarefa deletada com sucesso.")

    return redirect("list_reviews_me")


def show_review(request, id):
    review = get_object_or_404(Review, pk=id)
    return render(request, "reviews/show.html", {"review": review})

def media_autocomplete(request):
    term = request.GET["term"]
    medias = Media.objects.filter(name__icontains=term).values("id", "name")
    res = [{"value": media["id"], "label": media["name"]} for media in medias]

    return JsonResponse(res, safe=False)
