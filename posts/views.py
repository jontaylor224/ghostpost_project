from django.shortcuts import (render, get_object_or_404, redirect)
from .models import Post
from .forms import PostForm
import random
import string


def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_data = post_form.cleaned_data
            post = Post.objects.create(
                content=post_data.get('content'),
                is_boast=post_data.get('is_boast'),
                post_id=''.join(random.choice(string.ascii_lowercase)
                                for _ in range(6))
            )
            return redirect('../api/posts/{}/post_detail.html'.format(post.pk), pk=post.pk)
    else:
        post_form = PostForm()
    return render(request, 'posts/add_post.html', {'post_form': post_form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


def upvote(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.votes += 1
    post.save()
    return redirect('/')


def downvote(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.votes -= 1
    post.save()
    return redirect('/')


def delete_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    post.delete()
    return redirect('/')
