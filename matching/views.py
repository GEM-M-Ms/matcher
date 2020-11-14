from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from .utils import handle_upload_files



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload_files(request.FILES['file'])
            #redirect to success page
            return HttpResponseRedirect('/matching')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
