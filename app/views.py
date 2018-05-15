from django.shortcuts import render
from .models import Posts

# Create your views here.


def post_list(request):
    post_lists = Posts.objects.all()
    all_page = (len(post_lists) + 5 - 1) // 5
    currentpageid = (request.GET.get("page"))
    currentpage = 1
    if currentpageid != None:
        currentpage = int(currentpageid)
        if currentpage < 1:
            currentpage = 1
        elif currentpage > all_page:
            currentpage = all_page
    all = post_lists[currentpage * 5 - 5: currentpage * 5]
    prepage = currentpage - 1
    if prepage < 1:
        prepage = 1
    nextpage = currentpage + 1
    if nextpage > all_page:
        nextpage = all_page
    lastpage = all_page
    return render(request, 'post_list.html',{"all_Arts": all,"page":currentpage,"prepage":prepage,"nextpage": nextpage, "lastpage": lastpage})

