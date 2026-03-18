from django.shortcuts import render, get_object_or_404
from .models import Post

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'core/lista_posts.html', {'posts': posts})

def detalhe_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'core/detalhe_post.html', {'post': post})