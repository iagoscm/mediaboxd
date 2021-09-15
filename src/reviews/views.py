from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


@login_required
def list_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/list.html', {'reviews': reviews})


@login_required
def create_review(request):
    form = ReviewForm(request.POST or None)

    if form.is_valid():
        review = form.save(commit=False)
        review.author = request.user
        review.save()
        return redirect('list_reviews')
    
    return render(request, 'reviews/form.html', {'form': form})


@login_required
def update_review(request, id):
    review = Review.objects.get(id=id)
    form = ReviewForm(request.POST or None, instance=review)

    if form.is_valid():
        form.save()
        return redirect('list_reviews')

    return render(request, 'reviews/form.html', {'form': form, 'review': review})


@login_required
def delete_review(request, id):
    review = Review.objects.get(id=id)

    if request.method == 'POST':
        review.delete()
        return redirect('list_reviews')

    return render(request, 'review/delete-confirm.html', {'review': review})