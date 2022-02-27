from django.urls import path, include

from .views import *

app_name = 'scrapbook'


                    ### in use ###

urlpatterns = [
    path('scrapbook/', indexView),
    path('scrapbook/post/ajax/friend', postFriend, name = "post_friend"),
    path('scrapbook/get/ajax/validate/nickname', checkNickName, name = "validate_nickname"),
    path("cbv/", FriendView.as_view(), name = "friend_cbv")
]
