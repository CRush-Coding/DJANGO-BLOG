from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
import uuid
from django.db.models.signals import post_save

# Create your models here.


# Using base user model for now, with only Username and Password required
class User(AbstractUser):
    pass


# Want to upload profile pictures and media to seperate folders unique to each user

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.first_name, filename)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Title")
    caption = models.CharField(max_length=10000, verbose_name="Caption")
    date_posted = models.DateField(auto_now_add=True)
    date_edited = models.DateField(auto_now=True)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)


    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"{self.title} by {self.user}"

    def get_absolute_url(self):
        return reverse("postDetails", args=[str(self.id)])
    

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"

    # For clarification, follower is the current user and following is who they follow
    # e.g. If Timmy follows Johnny, follower = Timmy, Following = Johnny

class ShowPosts(models.Model):
    # Show all posts for follower from who they are following
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_followed")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user") 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    dateTime = models.DateTimeField()

    class Meta:
        verbose_name = "Show Post"
        verbose_name_plural = "Show Posts"

    def __str__(self):
        return f"Post by {self.post.user} for {self.user}"
    

    def send_post(sender, instance, created, **kwargs):
        # Attach each post to every user who follows the author of the post
        post = instance
        user = post.user
        date = post.date_posted
        # Sort by all users following the author
        followers = Follow.objects.all().filter(following=user)
        # Loop through all posts
        for person in followers:
            # Add a show post for that user
            send = ShowPosts(following=post.user, user=person.follower, post=post, dateTime=date)
            send.save()

post_save.connect(ShowPosts.send_post, sender=Post)

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Post_Author")
    time_posted = models.DateTimeField(auto_now_add=True)
    details = models.CharField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="Post")
            
