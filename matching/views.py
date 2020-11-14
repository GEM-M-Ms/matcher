from django.shortcuts import render

from .models import Cohort

def cohort_index(request):
    cohorts = Cohort.objects.all()
    context = {'cohorts': cohorts}
    return render(request, 'cohorts/index.html', context)
