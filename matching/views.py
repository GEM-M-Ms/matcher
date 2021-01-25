from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .models import Cohort, Mentee, Mentor, Match
from .utils import handle_mentee_files, handle_mentor_files
from .forms import MatchForm, CohortForm
from .utils import get_sorted_mentors_for_mentee

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
def create(request):
    if request.method == "POST":
        form = CohortForm(request.POST, request.FILES)

        if form.is_valid():
            with transaction.atomic():
                cohort = form.save()
                handle_mentee_files(form.cleaned_data['mentees_file'], cohort)
                handle_mentor_files(form.cleaned_data['mentors_file'], cohort)
                messages.success(request, 'Cohort created succesfully.')
                return redirect(reverse("show_cohort", kwargs={'cohort_id': cohort.id}))

    form = CohortForm()
    return render(request, "cohorts/create.html", {"form": form})

@login_required
def show_matches(request, cohort_id):
    cohort = get_object_or_404(Cohort, pk=cohort_id)
    matches = Match.objects.filter(cohort=cohort)
    return render(request, "cohorts/matches.html", {"cohort": cohort, "matches": matches})

@login_required
def new_match(request, cohort_id):
    cohort = get_object_or_404(Cohort, pk=cohort_id)

    if request.method == "POST":
        form = MatchForm(request.POST, cohort=cohort)

        if form.is_valid():
            match = form.save(commit=False)
            match.approver = request.user
            match.cohort = cohort
            match.save()
            return redirect(reverse("show_matches", kwargs={'cohort_id': cohort.id}))
    form = MatchForm(cohort=cohort)
    return render(request, "cohorts/new_match.html", {"cohort": cohort, "form": form})

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
def sorted_mentors(request, cohort_id):
    cohort = get_object_or_404(Cohort, pk=cohort_id)
    #hardcoded mentee atttributes atm
    mentors=get_sorted_mentors_for_mentee("15 15",cohort_id)
    return render(request, "cohorts/mentors.html", {"cohort": cohort, "mentors": mentors})
