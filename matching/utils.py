import csv
import io
import re

from .models import Mentee, Mentor
from .match_utils import calculate_diff

def convert_to_model_params(uploaded_file):
    file_bytes = uploaded_file.read().decode('utf-8')
    reader = csv.DictReader(io.StringIO(file_bytes))
    data = [line for line in reader]
    records = []
    for row in data:
        name = f"{row['First Name']} {row['Last Name']}"
        email = row["Email Address"]
        attributes = {}

        for key, value in row.items():
            if re.search(r'\d', key):
                numberless_key = re.sub(" \d+", "", key)
                attr_array = attributes.get(numberless_key, [])
                if value:
                    attr_array.append(value)
                attributes[numberless_key] = attr_array
            else:
                attributes[key] = value
        records.append((name, email, attributes))
    return records

def handle_mentee_files(uploaded_file, cohort):
    records = convert_to_model_params(uploaded_file)

    for record in records:
        name, email, attributes = record
        mentee = Mentee(name=name, email=email, cohort=cohort, other_attributes=attributes)
        mentee.save()


def handle_mentor_files(uploaded_file, cohort):
    records = convert_to_model_params(uploaded_file)

    for record in records:
        name, email, attributes = record
        mentor = Mentor(name=name, email=email, cohort=cohort, other_attributes=attributes)
        mentor.save()

def get_sorted_mentors_for_mentee(mentee_name,cohort):
    mentors = Mentor.objects.filter(cohort=cohort)
    mentee = Mentee.objects.filter(name__contains=mentee_name)
    print(mentee.count)
    the_mentee=mentee[0]
    print(the_mentee)
    print(mentors)
    return calculate_diff(the_mentee,mentors)

