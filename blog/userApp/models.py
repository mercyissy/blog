from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]

    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profilePictures/', null=True, blank=True)  # Added blank=True
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50, null=True)  # ✅ Removed comma
    country = models.CharField(max_length=50, null=True)
    date_of_birth = models.CharField(max_length=11, null=True)
    def __str__(self):

        
        return self.user.first_name + " " + self.user.last_name
    
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
