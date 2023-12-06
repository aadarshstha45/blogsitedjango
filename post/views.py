from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from post.models import Post
from post.forms import PostForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required


def post_view(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "postlist.html", context)


def mypost_view(request):
    id = request.user
    posts = Post.objects.filter(author=id)
    context = {"posts": posts}
    return render(request, "mypost.html", context)


def img_view(request, postid):
    posts = get_object_or_404(Post, id=postid)
    context = {"posts": posts}
    return render(request, "img.html", context)


@login_required
def post_add(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # print(form.cleaned_data)
        add = form.save(commit=False)
        add.author = request.user
        add.save()
        return HttpResponseRedirect(reverse("post:postlist"))
    return render(request, "postadd.html", {"form": form})


@login_required
def post_edit(request, postid):
    post = get_object_or_404(Post, id=postid)

    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("post:postlist"))
    return render(request, "postadd.html", {"form": form})


@login_required
def post_delete(request):
    postid = request.POST.get("postid")
    post = get_object_or_404(Post, id=postid)
    post.delete()
    return HttpResponseRedirect(reverse("post:postlist"))


def demo_for_ajax(request):
    data = {"name": "Ram", "address": "Ktm"}
    return JsonResponse(data, safe=False)
