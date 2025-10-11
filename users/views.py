from django.shortcuts import render, get_object_or_404 # Add get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import JsonResponse # New import for AJAX
from django.views.decorators.http import require_POST # New import for security

from .models import Post # Import your Post model


@login_required
def profile(request):
    return render(request, 'users/profile.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

# --- New Views for Likes/Dislikes ---

@require_POST
@login_required
def like_post(request, pk):
    """Handles the logic for liking and un-liking a post."""
    post = get_object_or_404(Post, id=pk)
    user = request.user

    # Toggle Like/Unlike
    if post.likes.filter(id=user.id).exists():
        # User already liked it, so unlike it
        post.likes.remove(user)
        liked_status = False
    else:
        # User is liking it
        post.likes.add(user)
        liked_status = True

        # If the user liked it, remove any existing dislike
        if post.dislikes.filter(id=user.id).exists():
            post.dislikes.remove(user)

    # Return the updated counts and status via JSON
    return JsonResponse({
        'status': 'ok',
        'is_liked': liked_status,
        'like_count': post.total_likes(),
        'dislike_count': post.total_dislikes(),
    })


@require_POST
@login_required
def dislike_post(request, pk):
    """Handles the logic for disliking and un-disliking a post."""
    post = get_object_or_404(Post, id=pk)
    user = request.user

    # Toggle Dislike/Un-dislike
    if post.dislikes.filter(id=user.id).exists():
        # User already disliked it, so un-dislike it
        post.dislikes.remove(user)
        disliked_status = False
    else:
        # User is disliking it
        post.dislikes.add(user)
        disliked_status = True

        # If the user disliked it, remove any existing like
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)

    # Return the updated counts and status via JSON
    return JsonResponse({
        'status': 'ok',
        'is_disliked': disliked_status,
        'like_count': post.total_likes(),
        'dislike_count': post.total_dislikes(),
    })