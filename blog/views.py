from django.shortcuts import render, get_object_or_404, redirect
from slugify import slugify
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from .forms import CommentForm, PostForm


# Create your views here.
def post_list(request):
    """
    Display a list of posts with pagination.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        Rendered HTML page with a list of posts.
    """
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug):
    """
    Display the details of a single post, including comments.
    
    Args:
        request: The HTTP request object.
        slug: The slug of the post.
    
    Returns:
        Rendered HTML page with post details and comments.
    """
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True)
    if request.user.is_authenticated:
        user_comments = post.comments.filter(author=request.user)
        comments = comments | user_comments

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # Save comment to the database
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user  # Associate the logged-in user
            comment.save()
            return redirect("post_detail", slug=slug)
    else:
        form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "form": form,
        },
    )


@login_required
def edit_comment(request, comment_id):
    """
    Edit an existing comment.
    
    Args:
        request: The HTTP request object.
        comment_id: The ID of the comment to edit.
    
    Returns:
        Rendered HTML page with the comment edit form.
    """
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure the user is the comment author
    if request.user != comment.author:
        return redirect("post_detail", slug=comment.post.slug)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post_detail", slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, "blog/edit_comment.html", {"form": form, "comment": comment})


@login_required
def delete_comment(request, comment_id):
    """
    Delete an existing comment.
    
    Args:
        request: The HTTP request object.
        comment_id: The ID of the comment to delete.
    
    Returns:
        Redirect to the post detail page after deletion.
    """
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure the user is the comment author
    if request.user != comment.author:
        return redirect("post_detail", slug=comment.post.slug)

    post_slug = comment.post.slug  # Store the post's slug before deletion
    comment.delete()
    return redirect("post_detail", slug=post_slug)


def loginView(request):
    """
    Handle user login.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        Rendered HTML page with the login form.
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Redirect to the profile or dashboard after successful login
            return redirect("profile")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


@login_required
def add_post(request):
    """
    Add a new post.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        Rendered HTML page with the post creation form.
    """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author to the logged-in user
            post.slug = slugify(post.title)  # Generate slug from title
            post.save()
            return redirect("post_list")  # Redirect after saving
    else:
        form = PostForm()

    return render(request, "blog/add_post.html", {"form": form})


@login_required
def edit_post(request, post_id):
    """
    Edit an existing post.
    
    Args:
        request: The HTTP request object.
        post_id: The ID of the post to edit.
    
    Returns:
        Rendered HTML page with the post edit form.
    """
    post = get_object_or_404(Post, id=post_id)

    # Ensure the user is the post author
    if request.user != post.author:
        return redirect("post_detail", slug=post.slug)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, "blog/edit_post.html", {"form": form, "post": post})


@login_required
def delete_post(request, post_id):
    """
    Delete an existing post.
    
    Args:
        request: The HTTP request object.
        post_id: The ID of the post to delete.
    
    Returns:
        Redirect to the post list page after deletion.
    """
    post = get_object_or_404(Post, id=post_id)

    # Ensure the user is the post author
    if request.user != post.author:
        return redirect("post_detail", slug=post.slug)

    post.delete()
    return redirect("post_list")
