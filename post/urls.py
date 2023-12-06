from django.urls import path, include
from post.views import (
    post_view,
    post_add,
    post_delete,
    post_edit,
    img_view,
    demo_for_ajax,
    mypost_view,
)

app_name = "post"

urlpatterns = [
    path("", post_view, name="postlist"),
    path("postadd/", post_add, name="postadd"),
    path("mypost/", mypost_view, name="mypost"),
    path("postedit/<int:postid>/", post_edit, name="postedit"),
    path("postdelete/", post_delete, name="postdelete"),
    path("demo-for-ajax/", demo_for_ajax, name="demo_for_ajax"),
    path("image/<int:postid>/", img_view, name="imgview"),
]
