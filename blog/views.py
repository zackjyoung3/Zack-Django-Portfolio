from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm

# index page
def blog_index(request):
    # query for the posts organized by the date that they were created on
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    # rendering the template with the context we just defined
    return render(request, "blog_index.html", context)

# all the blogs of a specific category
def blog_category(request, category):
    # query and get the posts that have the category passed in as a parameter
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    # for the context have the category and the posts that are assoociated with it
    context = {
        "category": category,
        "posts": posts
    }
    # rendering with the context just created
    return render(request, "blog_category.html", context)

# details for a specific blog post
def blog_detail(request, pk):
    # querying for the post with pk=pk
    post = Post.objects.get(pk=pk)
    # form that will be used for a user to leave a comment
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    # obtaining the comments for this post
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    # rendering with the post and its associated comments as the context
    return render(request, "blog_detail.html", context)

