from django.shortcuts import render
from .models import Post, Like
from django.http import HttpResponse
# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', { 'posts': posts })

def like(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(id = post_id )

        if likedpost.likes.count()>0:
            print("if part")
            print( likedpost.likes.count())
            likedpost.likes.all().delete()
            print("likes", likedpost.likes.count())
            return HttpResponse("unsuccesful")
        else:
            print("else part")
            m = Like( post=likedpost )
            m.save()
            print("likes", likedpost.likes.count())
            return HttpResponse('success')
    # else:
    #     return HttpResponse("unsuccesful")
