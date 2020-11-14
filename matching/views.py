from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from .utils import handle_mentee_files, handle_mentor_files, handle_return_mentor_files
from django.contrib import messages
from .models import Cohort


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def upload_file(request):
    if request.method == "POST":

        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid() and "mentee" in request.POST:
            # file is saved
            handle_mentee_files(request.FILES["file"])
            # redirect to success page
            return HttpResponseRedirect("/matching/data-upload")

        elif form.is_valid() and "mentor" in request.POST:
            # file is saved
            handle_mentor_files(request.FILES["file"])
            # redirect to success page
            return HttpResponseRedirect("/matching/data-upload")
        elif form.is_valid() and "mentor_return" in request.POST:
            # file is saved
            handle_return_mentor_files(request.FILES["file"])
            # redirect to success page
            return HttpResponseRedirect("/matching/data-upload")
    else:
        messages.error(request, "File is not CSV type")
        form = UploadFileForm()

    return render(request, "upload.html", {"form": form})


def cohort_index(request):
    cohorts = Cohort.objects.all()
    context = {"cohorts": cohorts}
    return render(request, "cohorts/index.html", context)
