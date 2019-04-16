from django.db import models
import time
from system.storage import ImageStorage


# Create your models here.


# 上传者
class UserInfo(models.Model):
    username = models.CharField(max_length=255, verbose_name='姓名')


# 上传的资料信息
class UploadInfo(models.Model):
    nickName = models.CharField(max_length=255, verbose_name='用户名', blank=False, null=False, unique=True)
    orderNumber = models.CharField(max_length=255, verbose_name='订单号', unique=True, blank=False, null=False)
    userImage = models.ImageField(upload_to='images', verbose_name='用户个人信息界面截图', blank=False, null=False,
                                  storage=ImageStorage())
    orderImage = models.ImageField(upload_to='images', verbose_name='订单界面截图', blank=False, null=False,
                                   storage=ImageStorage())
    is_active = models.BooleanField(default=False, verbose_name='是否通过审核')
    uploader = models.CharField(max_length=32, verbose_name='邀请人 (选填)')
    pubdatetime = models.DateTimeField(auto_now=True, verbose_name='上传时间')
    pubdate = models.DateField(auto_now=True, verbose_name='上传日期')
    payAccount = models.CharField(max_length=255, verbose_name='支付宝账号 (我方发放奖励金渠道)', blank=True, null=True)
    phoneNumber = models.BigIntegerField(verbose_name='手机号 (无支付宝账户可选填)', blank=True, null=True)
    filepath = models.CharField(verbose_name='上传Excel的文件路径', max_length=255, blank=True, null=True)
    imgpath = models.CharField(verbose_name='上传图片文件夹路径,以当日日期命名', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.orderNumber

    class Meta():
        verbose_name = '用户上传资料'
        verbose_name_plural = verbose_name
        ordering = ('-pubdate',)
