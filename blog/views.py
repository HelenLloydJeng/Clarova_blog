from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, CommentForm
from django.http import Http404, HttpResponse
# Import for cleaner error handling
from django.contrib.auth.decorators import login_required, user_passes_test


def home(request):
    return render(request, 'home.html')

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')  # newest first

    comment_form = CommentForm()

    if request.method == "POST":
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post_detail', pk=pk)
        else:
            return redirect('login')  # prevent anonymous comment post

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })


@user_passes_test(lambda user: user.is_staff or user.is_superuser)
# login_required is technically redundant if user_passes_test is used,
# but it's kept for clarity
@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)   # don't save yet
            post.author = request.user       # set the author
            post.save()                      # now save
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # DEFENSIVE DESIGN: Check if the user is authorized
    # ----------------------------------------------------
    if (
        request.user != post.author
        and not request.user.is_staff
        and not request.user.is_superuser
    ):
        # If the user is neither the author nor staff/admin,
        # raise a permission error
        # This is a key part of defensive design
        raise Http404("You are not authorized to edit this post.")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # ----------------------------------------------------
    # DEFENSIVE DESIGN: Check if the user is authorized
    # ----------------------------------------------------
    if (
        request.user != post.author
        and not request.user.is_staff
        and not request.user.is_superuser
    ):
        raise Http404("You are not authorized to delete this post.")
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
