from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from collections import namedtuple
from operator import  attrgetter

from .models import Mentee, Mentor, MatchConfig


#Health and Medicine
health_jobs = ['Alternative Medicine', 'Biotechnology', 'Hospital and Healthcare', 'Medical Practice' ,'Mental Health Care' ,'Pharmaceuticals' ,'Veterinary ']

Health_mentees = Mentee.objects.raw('SELECT * FROM matching_mentee WHERE Career_Field in %s', [health_jobs])
Health_mentors = Mentor.objects.raw('SELECT * FROM matching_mentee WHERE Career_Field in %s', [health_jobs])

#Business

business_jobs = ['Accounting','Banking', 'Capital Markets', 'Entrepreneurship', 'Financial Services', 'Human Resources','Insurance', 'Investment Banking/Management', 'Management Consulting', 'Marketing and Advertising', 'Market Research', 'Venture Capital and Private Equity']
Bus_mentees = Mentee.objects.raw('SELECT * FROM matching_mentee WHERE Career_Field in %s', [business_jobs])
Bus_mentors = Mentor.objects.raw('SELECT * FROM matching_mentee WHERE Career_Field in %s', [business_jobs])


#diff between mentee and mentor

  matching_fields = [
  ('Carrier', 'Industry', 1.),
  ('Hobbies', 'Hobbies', 0.5),
  ('Barriers', 'Barriers', 0.5),
  ('Describe Self','Describe Self',0.5),
  ('Town','Town',0.2),
  ('Etnicity','Etnicity',0.1),
  ('Religion', 'Religion', 0.1),
]

def ensure_match_config():
  if (MatchConfig.objects.all().count() == 0):
    for tpl in matching_fields:
      matchEntry = MatchConfig(mentee_column_name=tpl[0], mentor_column_name=tpl[1], weight=tpl[2])
      matchEntry.save()
  return MatchConfig.objects.all()

def calculate_diff(m):
  menteeAttr = m.other_attributes
  matchConfigs = ensure_match_config()
  l = []
  for mr in Mentor.objects.all():
    mentor_ratio=0
    mentorAttr = mr.other_attributes

    for tpl in matchConfigs:
      menteeValue = menteeAttr[tpl.mentee_column_name]
      mentorValue = mentorAttr[tpl.mentor_column_name]
      ratio=fuzz.token_set_ratio(menteeValue,mentorValue)
      mentor_ratio+=ratio*tpl.weight

    mentor_ratio/= len(matchConfigs)
    Entry = namedtuple('Entry','r m')
    entry = Entry(mentor_ratio,mr)
    l.append(entry)

  l.sort(key=attrgetter('r'), reverse=True)
  return [x[1] for x in l]
  #can also return list of tuples(ratio, mentor)
