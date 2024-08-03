from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from .models import Post, Comment, Like
from .forms import PostForm, CommentForm

# Create your views here.


def home(request):
    posts = Post.objects.all()
    post_form = PostForm()
    context = {"posts": posts, "form": post_form}
    return render(request, "index.html", context=context)


def add_post(request):
    if request.method == "POST":
        content = request.POST.get("post")
        user = request.user
        if content:
            post = Post.objects.create(post=content, author=user)
            if request.htmx:
                posts = Post.objects.all()
                html = render_to_string("partials/posts.html", {"posts": posts})
                return HttpResponse(html)
            else:
                return redirect("home")


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment_form = CommentForm()
    context = {"post": post, "form": comment_form}

    return render(request, "post-detail.html", context)


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            if request.htmx:
                comments = Comment.objects.filter(post=post).order_by("-created_at")
                html = render_to_string(
                    "partials/comments.html", {"comments": comments}
                )
                return HttpResponse(html)
    return redirect("post_detail", post_id=post_id)


@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        like.delete()

    if request.htmx:
        likes_count = post.total_likes
        return HttpResponse(likes_count)

    return redirect("post_detail", post_id=post_id)
