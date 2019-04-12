from django.shortcuts import render, HttpResponse
from yitaoApp.models import UploadInfo
from yitaoApp.forms import UploadForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def upload(request):
    if request.method == 'POST':
        uploadForm = UploadForm(request.POST, request.FILES)
        # 验证表单完整性
        if uploadForm.is_valid():
            form = uploadForm.save(commit=False)
            form.save()
            msg = '提交成功'
            return render(request, 'is_ok.html', {'msg': msg, 'success': 'True'})
        else:
            msg = uploadForm.errors
            return render(request, 'is_ok.html', {'msg': msg, 'success': 'False'})

    else:
        uploadForm = UploadForm()
        return render(request, 'upload.html', {'uploadForm': uploadForm})
