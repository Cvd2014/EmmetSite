from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(datePublished__lte=timezone.now()).order_by('datePublished')

    return render(request, "blog.html", {'posts': posts})
