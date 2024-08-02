from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.


def home(request):
    posts = Post.objects.all()
    post_form = PostForm()
    context = {"posts": posts, "form": post_form}
    return render(request, "index.html", context=context)


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form = PostForm()  # Reset the form after saving

            if request.htmx:
                posts = Post.objects.all()
                html = render_to_string("partials/posts.html", {"posts": posts})
                return HttpResponse(html)
        else:
            pass

        redirect('home')


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
            comment.user = request.user
            comment.save()

            if request.htmx:
                comments = post.comments.all()
                html = render_to_string(
                    "partials/comments.html", {"comments": comments}
                )
                return HttpResponse(html)
    return redirect("post_detail", post_id=post_id)

