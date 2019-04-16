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

