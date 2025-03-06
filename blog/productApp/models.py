from django.db import models
from blog.userApp.models import Profile
from django.contrib.auth.models import User

# class Blog(models.Model):
#     addedby = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     blog_title = models.CharField(max_length=255, null=True)
#     image = models.ImageField(upload_to='blogImages/', null=True, blank=True)
#     content = models.TextField(null=True)
#     ingredient = models.TextField(null=True)
#     category = models.CharField( max_length=20)
#     approved = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.blog_title


class Blog(models.Model):
    addedby = models.ForeignKey(Profile, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to='blogImages/', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    ingredient = models.TextField(null=True, blank=True)
    CATEGORY_CHOICES = [
        ('vegan', 'Vegan'),
        ('dessert', 'Dessert'),
        ('main_course', 'Main Course'),
        ('appetizer', 'Appetizer'),
        ('beverage', 'Beverage'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(null=True, blank=True) 
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title

