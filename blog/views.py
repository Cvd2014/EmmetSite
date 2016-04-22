from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Article, Video


# Create your views here.
# Blog Post List and Details
def post_list(request):
    posts = Post.objects.filter(datePublished__lte=timezone.now()).order_by('datePublished')

    return render(request, "blog.html", {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, 'posts.html', {'post': post})


# Article list and details
def article_list(request):
    articles = Article.objects.filter(datePublished__lte=timezone.now()).order_by('datePublished')
    return render(request, "article.html", {'articles': articles})

def video_list(request):
    videos= Video.objects.order_by('catagory')
    return render(request, "videos.html",{'videos':videos})


