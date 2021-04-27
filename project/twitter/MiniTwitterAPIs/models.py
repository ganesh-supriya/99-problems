
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):

    name = models.CharField(max_length=255,unique=True)
    email = models.CharField(max_length=255, unique=True )
    password = models.CharField(max_length=255, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.name

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=30)
    country = models.CharField(max_length=10)
    def __str__(self):
        return str(self.user)


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.content

class Follow(models.Model):

    followers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    followings = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    class Meta:
        unique_together = ('followers', 'followings')
    def __str__(self):
        return str(self.followers)


class TweetLike(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='tweet_likes')
    def __str__(self):
        return str(self.user)

class TweetComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='tweet_comments')
    comment = models.TextField(max_length=255,blank=True,null=True)

    def __str__(self):
        return str(self.user)
    def __str__(self):
        return str(self.comment)





