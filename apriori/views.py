from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from apriori.proces import proces
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

main = proces()
@login_required
def home(request):
    return render(request, 'html/home.html',{'sidebar':'dashboard'})

@login_required
def upload(request):
    if request.method == 'POST' and 'upload' in request.FILES:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save("file/data.csv", upload)
        file_url = fss.url(file)
        json = main.read_data('.'+file_url)
        return render(request, 'html/upload-data.html', {'data':json,'sidebar':'upload'})
    return render(request, 'html/upload-data.html',{'sidebar':'upload'})

@login_required
def train(request):
    if request.method == 'POST':
        input = {
            'support':request.POST.get('support'),
            'confidence':request.POST.get('confidence')
        }
        result = main.train(input)
        return render(request, 'html/train.html',{'data':result,'sidebar':'train'})
    return render(request, 'html/train.html',{'sidebar':'train'})