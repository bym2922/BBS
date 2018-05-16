from django.shortcuts import render
from .models import Post

# Create your views here.

# def post_list(request):
#     post_lists = Posts.objects.all()
#     all_page = (len(post_lists) + 5 - 1) // 5
#     currentpageid = (request.GET.get("page"))
#     currentpage = 1
#     if currentpageid != None:
#         currentpage = int(currentpageid)
#         if currentpage < 1:
#             currentpage = 1
#         elif currentpage > all_page:
#             currentpage = all_page
#     all = post_lists[currentpage * 5 - 5: currentpage * 5]
#     prepage = currentpage - 1
#     if prepage < 1:
#         prepage = 1
#     nextpage = currentpage + 1
#     if nextpage > all_page:
#         nextpage = all_page
#     lastpage = all_page
#     return render(request, 'post_list.html',{"all_Posts": all,"page":currentpage,"prepage":prepage,"nextpage": nextpage, "lastpage": lastpage})
#
#
# def add_post(request):
#     return render(request, 'add_post.html')
#
#
# def get_add_data(request):
#     name = request.POST.get("auth")
#     all_auth = Author.objects.filter(name=name)
#     if all_auth.__len__() != 0:
#         for au in all_auth:
#             if name == au.name:
#                 count = Author.objects.get(name=name).art_nums
#                 count += 1
#                 auth = Author.objects.get(name=name)
#                 auth.art_nums = count
#                 break
#             else:
#                 auth = Author(name=name, art_nums=1)
#         auth.save()
#         author = Author.objects.get(name=name).id
#     else:
#         auth = Author(name=name, art_nums=1)
#         auth.save()
#         author = Author.objects.get(name=name).id
#     title = request.POST.get("tit")
#     # summary = request.POST.get("sum")
#     content = request.POST.get("cont")
#     a = Posts(title=title, author_id=author, content=content)
#     a.save()
#     return post_list(request)

# coding: utf-8
from math import ceil

from django.shortcuts import render, redirect

# from post.models import Post


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


def read(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)
    return render(request, 'read_post.html', {'post': post})


def search(request):
    keyword = request.POST.get('keyword')
    posts = Post.objects.filter(content__contains=keyword)
    return render(request, 'search.html', {'posts': posts})