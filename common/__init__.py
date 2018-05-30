# coding: utf-8

from redis import Redis
from django.conf import settings
# from bbs import settings

rds = Redis(**settings.REDIS)  # 创建 Redis 实例

