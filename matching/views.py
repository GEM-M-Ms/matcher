from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cohort, Mentee, Mentor
from .utils import handle_mentee_files, handle_mentor_files
from .forms import UploadFileForm

@login_required
def index(request):
    cohorts = Cohort.objects.all()
    return render(request, "cohorts/index.html", {"cohorts": cohorts})

@login_required
def show(request, cohort_id):
    cohort = get_object_or_404(Cohort, pk=cohort_id)
    request.session['cohort_id'] = cohort_id
    return render(request, "cohorts/show.html", {"cohort": cohort})

@login_required
def show_matching1(request): 
    if 'cohort_id' in request.session:
        cohort_id = request.session['cohort_id']
        mentee_list = Mentee.objects.get(cohort_id=cohort_id)
        mentor_list = Mentor.objects.get(cohort_id=cohort_id)
    else: 
        messages.warning(request, 'To narrow your findings, please select a cohort from the main page')
        mentee_list = Mentee.objects.all()
        mentor_list = Mentor.objects.all()

    context_dict = {'Mentees': mentee_list, 'Mentors':mentor_list}
    return render(request, "match/match1.html", {"context_dict":context_dict})

@login_required
def upload(request):
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
