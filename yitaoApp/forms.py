from django import forms
from yitaoApp.models import UploadInfo
import time


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadInfo
        fields = (
            'nickName', 'orderNumber', 'userImage', 'orderImage',
            'uploader', 'payAccount', 'phoneNumber',
        )

    # def __init__(self):
    #     date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[:-9]
    #     self.filepath = filepath = './media/files/' + date + '.xls'
