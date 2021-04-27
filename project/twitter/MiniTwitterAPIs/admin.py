from django.contrib import admin

from MiniTwitterAPIs.models import UserProfile, Tweet, Follow, TweetLike, TweetComment

admin.site.register(UserProfile)
admin.site.register(Tweet)
admin.site.register(Follow)
admin.site.register(TweetLike)
admin.site.register(TweetComment)