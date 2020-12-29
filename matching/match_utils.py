from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from collections import namedtuple
from operator import  attrgetter
import re

from .models import Mentee, Mentor, MatchConfig


#Health and Medicine
health_jobs = ['Alternative Medicine', 'Biotechnology', 'Hospital and Healthcare', 'Medical Practice' ,'Mental Health Care' ,'Pharmaceuticals' ,'Veterinary']
#Business
business_jobs = ['Accounting','Banking', 'Capital Markets', 'Entrepreneurship', 'Financial Services', 'Human Resources','Insurance', 'Investment Banking/Management', 'Management Consulting', 'Marketing and Advertising', 'Market Research', 'Venture Capital and Private Equity']
#Urban Design
urban_jobs = ['Architecture/Planning','Civil Engineering']
#IT
it_jobs=['Graphic Design ','Information technology and Services']
#Social Services
social_jobs = ['Civil/Social Organization','Fundraising','Non-profit Organization Management','Philanthropy','Program Development','Social Work']
#Real Estate
real_estate_jobs = ['Commercial Real Estate','Real estate']
#Military
military_jobs = ['Defence and Space','Military']
#Education
education_jobs = ['Education','Higher Education','Libraries','Museums and Institutions','Research']
#Sales/Goods and Services
sales_jobs = ['Business Supplies and Equipment','Consumer Electronics','Consumer Goods and Services','Cosmetics','Farming','Furniture','Import and Export','Retail','Supermarkets']
#Service Industry
service_jobs = ['Gambling and Casinos','Hospitality','Leisure, Travel and Tourism','Restaurants']
#Creative/Media
creative_media_jobs = ['Animation','Apparel/Fashion','Arts (Visual)','Broadcast Media','Entertainment','Events Services','Film Production','Motion Pictures and Film','Music','Newspapers','Performing Arts','Photography','Publishing','Public Relations and Communications','Telecommunications','Writing and Editing']
#Government/Foreign Affairs
government_foreign_jobs = ['Executive Office','Government Administration','Government Relations','International Affairs','International Trade and Development','Legislative Office','Political Organization','Public Policy']
#Legal
legal_jobs = ['Judiciary','Law (Practice)']
#Law Enforcement
law_enforcement_jobs = ['Law Enforcement','Security and Investigations']
#Professional Sports/Fitness
sports_fitness_jobs = ['Health, Wellness and Fitness','Professional Training and Coaching','Recreational Facilities and Services','Sporting Goods']
#Industrial Production
industrial_production_jobs = ['Automotive','Building Materials','Chemicals','Glass, Ceramics, and Concrete','Industrial Automation','Logistics and Supply Chain','Mechanical or Industrial Engineering','Oil and Energy','Renewables and Environment']
#Miscellaneous
misc_jobs = ['Miscellaneous','Maritime','Religious Institutions','Translation and Localization']


#industry_types
industry_types = [
  ('HEALTH',health_jobs),
  ('BUSINESS',business_jobs),
  ('URBAN',urban_jobs),
  ('IT',it_jobs),
  ('SOCIAL',social_jobs),
  ('REAL_ESTATE',real_estate_jobs),
  ('MILITARY',military_jobs),
  ('EDUCATION',education_jobs),
  ('SALES',sales_jobs),
  ('SERVICE',service_jobs),
  ('CREATIVE_MEDIA',creative_media_jobs),
  ('GOVERNMENT_FOREGIN_AFFAIRS',government_foreign_jobs),
  ('LEGAL',legal_jobs),
  ('LAW_ENFIRCEMENT',law_enforcement_jobs),
  ('SPORTS_FITNESS',sports_fitness_jobs),
  ('INDUSTRIAL',industrial_production_jobs),
  ('MISC',misc_jobs),
]


#diff between mentee and mentor

matching_fields = [
  ('Career','Current Industry', 1.),
  ('Hobbies', 'Hobbies', 0.5),
  ('Barriers', 'Barriers', 0.5),
  ('Describe Self','Describe Self',0.5),
  ('City/Town (City of Toronto, Durham, Halton, Peel, York)','Town',0.2),
  ('Ethnicity','Ethnicity',0.1),
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

      ratio=0
      #check for absent value
      if isNotBlank(menteeValue) and isNotBlank(mentorValue):
        #atm check that mentor carreer matches one of mentee
        if type(mentorValue) == 'str' and type(menteeValue) == 'list':
          ratio=find_one_entry_in_list(mentorValue,menteeValue)
        else:
          ratio=fuzz.token_set_ratio(mentorValue,menteeValue)
      mentor_ratio+=ratio*tpl.weight

    mentor_ratio/= len(matchConfigs)
    Entry = namedtuple('Entry','r m')
    entry = Entry(mentor_ratio,mr)
    l.append(entry)

  l.sort(key=attrgetter('r'), reverse=True)
  return [x[1] for x in l]
  #can also return list of tuples(ratio, mentor)

def isNotBlank (s):
  return bool([re.sub('[^a-zA-Z0-9]+', '', _) for _ in s])

#rate would be 100 or 0
def find_one_entry_in_list (mentorValue,menteeValue):
  #fix mismatch: menteeValue=['Education', 'Writing & Editing', 'Law (Practice)'] mentorValue=Law Practice mentor=12 12
  mteeValue=normalize(menteeValue)
  if mentorValue in mteeValue:
    return 100
  else:
    return 0

def normalize(s):
  return [re.sub('[^a-zA-Z0-9 ]+', '', _) for _ in s]
