from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
# Create your views here.
def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})


def post_detail(request,pk):#This time our view is given an extra parameter pk. Our view needs to catch it, right?(this name should be same as that we used in urls.py)
    post=get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})
