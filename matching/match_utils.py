from .models import Mentee, Mentor


#Health and Medicine
health_jobs = ['Alternative Medicine', 'Biotechnology', 'Hospital and Healthcare', 'Medical Practice' ,'Mental Health Care' ,'Pharmaceuticals' ,'Veterinary ']

Health_mentees = Mentee.objects.raw('SELECT * FROM matching_mentee WHERE Career_Field in %s', [health_jobs])
Health_mentors = Mentor.objects.raw('SELECT * FROM matching_mentee WHERE Career_Field in %s', [health_jobs])

#Business

business_jobs = ['Accounting','Banking', 'Capital Markets', 'Entrepreneurship', 'Financial Services', 'Human Resources','Insurance', 'Investment Banking/Management', 'Management Consulting', 'Marketing and Advertising', 'Market Research', 'Venture Capital and Private Equity']
Bus_mentees = Mentee.objects.raw('SELECT * FROM matching_mentee WHERE Career_Field in %s', [business_jobs])
Bus_mentors = Mentor.objects.raw('SELECT * FROM matching_mentee WHERE Career_Field in %s', [business_jobs])

from .models import Mentee, Mentor


# Health and Medicine
health_jobs = [
    "Alternative Medicine",
    "Biotechnology",
    "Hospital and Healthcare",
    "Medical Practice",
    "Mental Health Care",
    "Pharmaceuticals",
    "Veterinary ",
]

Health_mentees = Mentee.objects.raw(
    "SELECT * FROM matching_mentee WHERE Career_Field in %s", [health_jobs]
)
Health_mentors = Mentor.objects.raw(
    "SELECT * FROM matching_mentee WHERE Career_Field in %s", [health_jobs]
)

# Business

business_jobs = [
    "Accounting",
    "Banking",
    "Capital Markets",
    "Entrepreneurship",
    "Financial Services",
    "Human Resources",
    "Insurance",
    "Investment Banking/Management",
    "Management Consulting",
    "Marketing and Advertising",
    "Market Research",
    "Venture Capital and Private Equity",
]
Bus_mentees = Mentee.objects.raw(
    "SELECT * FROM matching_mentee WHERE Career_Field in %s", [business_jobs]
)
Bus_mentors = Mentor.objects.raw(
    "SELECT * FROM matching_mentee WHERE Career_Field in %s", [business_jobs]
)
