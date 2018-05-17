from django.core.cache import cache
from common.keys import VIEW_KEY

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
