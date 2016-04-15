from django.shortcuts import render
from blog.models import Post, Article
from django.utils import timezone


# Create your views here.
def get_index(request):
    last_post = Post.objects.filter(datePublished__lte=timezone.now()).order_by('-datePublished')[0]
    last_article = Article.objects.filter(datePublished__lte=timezone.now()).order_by('-datePublished')[0]
    return render(request, "index.html", {'last_post': last_post, 'last_article': last_article})
