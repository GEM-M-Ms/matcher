from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cohort, Mentee, Mentor, Match
from .utils import handle_mentee_files, handle_mentor_files
from .forms import MatchForm, UploadFileForm

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
def show_matches(request, cohort_id):
    cohort = get_object_or_404(Cohort, pk=cohort_id)
    matches = Match.objects.filter(cohort=cohort)
    return render(request, "cohorts/matches.html", {"cohort": cohort, "matches": matches})

@login_required
def new_match(request, cohort_id):
    cohort = get_object_or_404(Cohort, pk=cohort_id)
    unmatched_mentees = Mentee.objects.filter(cohort=cohort, match__mentee__isnull=True)
    unmatched_mentors = Mentor.objects.filter(cohort=cohort, match__mentor__isnull=True)
    form = MatchForm()
    return render(request, "cohorts/new_match.html", {"unmatched_mentees": unmatched_mentees, "unmatched_mentors": unmatched_mentors, "cohort": cohort, "form": form})

@login_required
def show_mentees(request, cohort_id):
    cohort = get_object_or_404(Cohort, pk=cohort_id)
    mentees = Mentee.objects.filter(cohort=cohort)
    return render(request, "cohorts/mentees.html", {"cohort": cohort, "mentees": mentees})

@login_required
def show_mentors(request, cohort_id):
    cohort = get_object_or_404(Cohort, pk=cohort_id)
    mentors = Mentor.objects.filter(cohort=cohort)
    return render(request, "cohorts/mentors.html", {"cohort": cohort, "mentors": mentors})

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
