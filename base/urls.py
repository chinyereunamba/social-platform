from django.urls import path
from .views import home, add_post, post_detail, add_comment


urlpatterns = [
    path("", home, name="home"),
    path("add-post/", add_post, name="add_post"),
    path("post/<int:post_id>/", post_detail, name="post"),
    path("add-comment/<int:post_id>/", add_comment, name="add_comment"),
]
