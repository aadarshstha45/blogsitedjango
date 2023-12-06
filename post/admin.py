from django.contrib import admin
from post.models import Post
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "body",
        "image",
        "author",
    )

    list_filter = ("author",)

    search_fields = ("author",)
