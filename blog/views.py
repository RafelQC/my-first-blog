from django.shortcuts import render
from django.utils.timezone import now
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
