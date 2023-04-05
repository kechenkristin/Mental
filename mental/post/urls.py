from django.urls import path

from .views import CreatePostView, post_list  # new

urlpatterns = [
    path("list/", post_list, name="post_list"),
    path("add/", CreatePostView.as_view(), name="add_post")  # new
]
