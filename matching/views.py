from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .utils import handle_mentee_files, handle_mentor_files
from .models import Cohort
from .forms import UploadFileForm

@login_required
def index(request):
    cohorts = Cohort.objects.all()
    return render(request, "cohorts/index.html", {"cohorts": cohorts})

@login_required
def show(request, cohort_id):
    cohort = get_object_or_404(Cohort, pk=cohort_id)
    return render(request, "cohorts/show.html", {"cohort": cohort})

@login_required
def upload(request, cohort_id):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        cohort = get_object_or_404(Cohort, pk=cohort_id)

        if form.is_valid():
            if "mentee" in request.POST:
                handle_mentee_files(request.FILES["file"], cohort)
            elif "mentor" in request.POST:
                handle_mentor_files(request.FILES["file"], cohort)
            messages.success(request, 'File successfully uploaded.')
            return redirect(reverse("upload", kwargs={'cohort_id': cohort.id}))
        else:
            messages.error(request, "File is not CSV type")
    else:
        form = UploadFileForm()
    return render(request, "forms/upload.html", {"form": form})
