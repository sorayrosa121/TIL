from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib import messages

# Create your views here.

@require_safe
def index(request):
    reviews = Review.objects.order_by('-pk')    
    # reviews = Review.objects.all()    
    context ={
        'reviews': reviews
    }
    return render(request, 'community/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid:
            review = form.save()
            messages.info(request, '리뷰가 작성되었습니다.')
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context= {
        'form': form,
    }
    return render(request, 'community/form.html', context)

@require_safe
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    context= {
        'review': review,
    }
    return render(request, 'community/detail.html', context)

@require_http_methods(['GET', 'POST'])
def update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid:
            review = form.save()
            messages.info(request, '리뷰가 수정되었습니다.')
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm(instance=review)
    context= {
        'form': form,
        'review': review,
    }
    return render(request, 'community/update.html', context)

@ require_POST
def delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    return redirect('community:index')