from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib import messages
from .models import Post, Category
from .forms import PostForm, CommentForm

# Create your views here.
def home(request):
    """Home page view displaying published posts"""
    posts = Post.objects.filter(status='published')
    categories = Category.objects.all()
    
    return render(request, 'blog/home.html', {
        'posts': posts,
        'categories': categories
    })

def post_detail(request, pk):
    """View for displaying a single post and its comments"""
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True)
    
    # Comment form handling
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid() and request.user.is_authenticated:
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post and user
            new_comment.post = post
            new_comment.author = request.user
            # Save the comment to the database
            new_comment.save()
            messages.success(request, 'Your comment has been added.')
            return redirect('blog:post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def post_new(request):
    """View for creating a new post"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            # Save the many-to-many data for categories
            form.save_m2m()
            messages.success(request, 'Your post has been created!')
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'blog/post_edit.html', {
        'form': form,
        'title': 'New Post'
    })

@login_required
def post_edit(request, pk):
    """View for editing an existing post"""
    post = get_object_or_404(Post, pk=pk)
    
    # Check if the current user is the author
    if post.author != request.user:
        messages.error(request, 'You can only edit your own posts.')
        return redirect('blog:post_detail', pk=post.pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            # Save the many-to-many data for categories
            form.save_m2m()
            messages.success(request, 'Your post has been updated!')
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_edit.html', {
        'form': form,
        'post': post,
        'title': 'Edit Post'
    })

@login_required
def post_delete(request, pk):
    """View for deleting a post"""
    post = get_object_or_404(Post, pk=pk)
    
    # Check if the current user is the author
    if post.author != request.user:
        messages.error(request, 'You can only delete your own posts.')
        return redirect('blog:post_detail', pk=post.pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted!')
        return redirect('blog:home')
    
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

def category_posts(request, category):
    """View for displaying posts filtered by category"""
    category_obj = get_object_or_404(Category, slug=category)
    posts = Post.objects.filter(categories=category_obj, status='published')
    
    return render(request, 'blog/category_posts.html', {
        'category': category_obj,
        'posts': posts
    })
