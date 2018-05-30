from django.core.cache import cache
from common.keys import VIEW_KEY, READ_RANK_KEY
from common import rds
from .models import Post


def page_cache(n):
    def wrap1(view_func):
        def wrap2(request):
            key = VIEW_KEY % request.get_full_path()
            response = cache.get(key)
            print('从缓存获取数据：%s'% response)
            if response is None:
                response = view_func(request)
                print('缓存不存在，从数据库获取：%s' % response)
                cache.set(key, response, n)
                response1 = cache.get(key)
                print('================', response1)
            return response
        return wrap2
    return wrap1

def read_count(read_view_func):
    def count(request):
        response = read_view_func(request)
        if response.status_code <= 300:
            post_id = request.GET.get('post_id')
            rds.zincrby(READ_RANK_KEY, post_id)
        return response
    return count


def get_top_n(count):
    # 原始数据
    ori_data = rds.zrevange(READ_RANK_KEY, 0, count - 1, withscores=True)
    # rank_data = [
    #     [21, 39],
    #     [19, 27],
    #     [15, 20],
    #     ...
    # ]
    # 整理后的排名
    rank_data = [[int(post_id),int(count)] for post_id,count in ori_data]
    post_id_list = [post_id for post_id, _ in rank_data]
    # 获取文章
    posts = Post.objects.filter(id__in=post_id_list)
    # 对posts按post_id_list顺序排序
    posts = sorted(posts, key=lambda post : post_id_list.index(post.id))
    # 替换每一项的 post_id 为post实例
    for item, post in zip(rank_data, posts):
        item[0] = post
    return rank_data
