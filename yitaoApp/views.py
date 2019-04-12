from django.shortcuts import render, HttpResponse
from yitaoApp.models import UploadInfo
from yitaoApp.forms import UploadForm
from yitaoApp.tools import toExcel, getData
from django.http import FileResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


# 上传文件
def upload(request):
    if request.method == 'POST':
        uploadForm = UploadForm(request.POST, request.FILES)
        # 验证表单完整性
        if uploadForm.is_valid():
            # 拿到表格数据
            values = getData(dict(request.POST))
            # 导出Excel表
            filepath = toExcel(values)
            form = uploadForm.save(commit=False)
            form.filepath = filepath
            form.save()
            # 存储文件路径
            msg = '提交成功'

            return render(request, 'is_ok.html', {'msg': msg, 'success': 'True'})
        else:
            msg = uploadForm.errors
            return render(request, 'is_ok.html', {'msg': msg, 'success': 'False'})

    else:
        uploadForm = UploadForm()
        return render(request, 'upload.html', {'uploadForm': uploadForm})


# 展示文件列表
def showfiles(request):
    all_files = UploadInfo.objects.all().values('pubdate', 'filepath').distinct().order_by('-pubdate')
    ctx = {
        'files': all_files
    }
    print(len(all_files))
    return render(request, 'showfiles.html', ctx)


# 下载Excel文件
def download(request, filepath):
    file = open(filepath, 'rb')
    filename = filepath.split('/')[-1]
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=' + filename
    return response
