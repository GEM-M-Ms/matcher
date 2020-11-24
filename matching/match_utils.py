from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from collections import namedtuple
from operator import  attrgetter

from .models import Mentee, Mentor


#Health and Medicine
health_jobs = ['Alternative Medicine', 'Biotechnology', 'Hospital and Healthcare', 'Medical Practice' ,'Mental Health Care' ,'Pharmaceuticals' ,'Veterinary ']

Health_mentees = Mentee.objects.raw('SELECT * FROM matching_mentee WHERE Career_Field in %s', [health_jobs])
Health_mentors = Mentor.objects.raw('SELECT * FROM matching_mentee WHERE Career_Field in %s', [health_jobs])

#Business

business_jobs = ['Accounting','Banking', 'Capital Markets', 'Entrepreneurship', 'Financial Services', 'Human Resources','Insurance', 'Investment Banking/Management', 'Management Consulting', 'Marketing and Advertising', 'Market Research', 'Venture Capital and Private Equity']
Bus_mentees = Mentee.objects.raw('SELECT * FROM matching_mentee WHERE Career_Field in %s', [business_jobs])
Bus_mentors = Mentor.objects.raw('SELECT * FROM matching_mentee WHERE Career_Field in %s', [business_jobs])


#differense between mentee and mentor
matching_fields = ['Hobbies','Barriers']

def calculate_diff(m):
  menteeAttr = m.other_attributes
  l = []
  for mr in Mentor.objects.all():
    mentor_ratio=0
    mentorAttr = mr.other_attributes

    for wr in matching_fields:
      menteeValue = menteeAttr[wr]
      mentorValue = mentorAttr[wr]
      ratio=fuzz.token_set_ratio(menteeValue,mentorValue)
      mentor_ratio+=ratio

    mentor_ratio/= len(matching_fields)
    Entry = namedtuple('Entry','r m')
    entry = Entry(mentor_ratio,mr)
    l.append(entry)

  l.sort(key=attrgetter('r'), reverse=True)
  return [x[1] for x in l]
  #can also return list of tuples(ratio, mentor)
