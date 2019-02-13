from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    detail = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'detail': detail})
