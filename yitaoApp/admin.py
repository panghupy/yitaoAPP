from django.contrib import admin
from yitaoApp.models import UploadInfo
from daterange_filter.filter import DateRangeFilter


# Register your models here.


class UploadInfoAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ['is_active', 'uploader', ('pubdate', DateRangeFilter)]

    list_display = ['orderNumber', 'nickName', 'userImage', 'orderImage', 'is_active', 'uploader']


admin.site.register(UploadInfo, UploadInfoAdmin)
