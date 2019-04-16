# -*- coding: UTF-8 -*-
from django.core.files.storage import FileSystemStorage
import os, time

date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[:-9]


class ImageStorage(FileSystemStorage):
    from django.conf import settings

    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        # 初始化
        super(ImageStorage, self).__init__(location, base_url)

    # 重写 _save方法
    def _save(self, name, content):
        # 文件扩展名
        ext = os.path.splitext(name)[-1]
        # 以当前日期命名的文件夹
        dirpath = './media/images/' + date
        # 如果不存在则创建文件夹
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)
        d = os.path.dirname(name) + '/' + date + '/'
        fn = open('./system/user.txt').read()
        # 重写合成文件名
        name = os.path.join(d, fn + ext)
        # 调用父类方法
        return super(ImageStorage, self)._save(name, content)
