from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    """Form for creating and editing blog posts"""
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image', 'categories', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    """Form for adding comments to posts"""
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Add your comment here...'}),
        }
        labels = {
            'content': 'Comment',
        }

