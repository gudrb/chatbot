from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from .models import Post


def post_list(request):
    return JsonResponse({
        'type': "buttons",
        'buttons': ["선택1", "선택2", "선택3"],
    })
'''
# Create your views here.
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_list(request):
    return render(request, 'blog/post_list.html', {})
'''
'''
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_list(request):
    posts=Post.objects.filter(published_data__lte=timezone.now()).order_by('published_data')
    return render(request, 'blog/post_list.html', {'posts':posts})
    return JsonResponse({
            'type' : "buttons",
            'buttoens' :["선택1","선택2","선택3"],
'''