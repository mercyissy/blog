from django import forms
from .models import Blog

from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'blog_title',
            'content',
            'ingredient',
            'category',
            'description',
            'image',
        ]

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control mb-2'}),
            'ingredient': forms.Textarea(attrs={'rows': 20, 'class': 'form-control mb-2'}),
            'category': forms.Select(attrs={'class': 'form-control mb-2'}),  # Use Select for category
            'description': forms.Textarea(attrs={'class': 'form-control mb-2'}),  # Apply attrs to description
            'image': forms.FileInput(attrs={'class': 'form-control mb-2'}),
        }


    