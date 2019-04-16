from django.shortcuts import render, HttpResponse
from yitaoApp.models import UploadInfo
from yitaoApp.forms import UploadForm
from yitaoApp.tools import toExcel, getData, toZip
from django.http import FileResponse
from wsgiref.util import FileWrapper


# Create your views here.
def index(request):
    return render(request, 'index.html')


# 拿到image文件名

# 上传文件
def upload(request):
    if request.method == 'POST':
        uploadForm = UploadForm(request.POST, request.FILES)

        # 验证表单完整性
        if uploadForm.is_valid():
            # 记录用户名，以便于给上传的图片重新命名
            with open('./system/user.txt', 'w')as f:
                f.write(request.POST['nickName'])
            # 拿到表格数据
            values = getData(dict(request.POST))
            # 导出Excel表
            filepath = toExcel(values)
            imgpath = './media/images/' + filepath.split('/')[-1].split('.')[0]
            print('imgpath', imgpath)
            form = uploadForm.save(commit=False)
            form.imgpath = imgpath
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
    all_files = UploadInfo.objects.all().values('pubdate', 'filepath', 'imgpath').distinct().order_by('pubdate')
    ctx = {
        'files': all_files
    }
    print(len(all_files))
    return render(request, 'showfiles.html', ctx)


# 下载Excel文件
def download_file(request, filepath):
    file = open(filepath, 'rb')
    filename = filepath.split('/')[-1]
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=' + filename
    return response


# 下载图片

def download_images(request, filedate):
    '''
    :param filedate: 前段传过来的是图片文件夹的路径,即日期,eg: './media/images/2019-04-12'
    :return:
    '''
    print('-' * 100)
    print(filedate)
    filepath = toZip(filedate)
    file = open(filepath, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=' + filepath.split('/')[-1]
    return response
