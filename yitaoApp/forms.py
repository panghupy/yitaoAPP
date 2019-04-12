from django import forms
from yitaoApp.models import UploadInfo


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadInfo
        fields = (
            'nickName', 'orderNumber', 'userImage', 'orderImage',
            'uploader', 'payAccount', 'phoneNumber'
        )
