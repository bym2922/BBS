# coding: utf-8

from django.shortcuts import render, redirect

from math import ceil

from .models import Post,Comment
from  post.helper import page_cache
from  user.helper import login_required

# Create your views here.


def post_list(request):
    page = int(request.GET.get('page', 1))  # 页码

    total = Post.objects.count()  # 文章总数
    per_page = 10                   # 每页文章数
    pages = ceil(total / per_page)  # 总页数

    start = (page - 1) * per_page
    end = start + per_page

    # SELECT * FROM post OFFSET start LIMIT 5
    posts = Post.objects.all().order_by('-id')[start:end]

    return render(request, 'post_list.html', {'posts': posts, 'pages': range(pages)})

@login_required
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
        return redirect('/read_post/?post_id=%s' % post.id)
    else:
        return render(request, 'add_post.html')


def edit(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('/read_post/?post_id=%s' % post.id)
    else:
        post_id = request.GET.get('post_id')
        post = Post.objects.get(id=post_id)
        return render(request, 'edit_post.html', {'post': post})

@page_cache(5)
def read(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)
    return render(request, 'read_post.html', {'post': post})


def search(request):
    keyword = request.POST.get('keyword')
    posts = Post.objects.filter(content__contains=keyword)
    return render(request, 'search.html', {'posts': posts})

@login_required
def comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        content = request.POST.get('content')
        Comment.objects.create(uid=request.session['uid'], post_id=post_id, content=content)
    return redirect('/read_post/?post_id=%s' % post_id)

def top10(request):

    return render(request,'top10.html',{})

