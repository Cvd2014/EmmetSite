from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(datePublished__lte=timezone.now()).order_by('datePublished')

    return render(request, "blog.html", {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    #post.views += 1
    post.save()
    return render(request, 'posts.html', {'post': post})