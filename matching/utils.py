import csv
import io
import json
from .models import Mentor

def convert_to_dicts(uploaded_file):
    file_bytes = uploaded_file.read().decode('utf-8')
    reader = csv.DictReader(io.StringIO(file_bytes))
    return [line for line in reader]

def handle_mentee_files(uploaded_file):
    data = convert_to_dicts(uploaded_file)
    print(data)


def handle_mentor_files(uploaded_file):
    data = convert_to_dicts(uploaded_file)
    print(data)
    for dict_line in data:
        print(dict_line["Personal Email Address"])
        print(json.dumps(dict_line))
        mentor = Mentor(name=dict_line["First Name"] + " " + dict_line["Last Name"], email=dict_line["Personal Email Address"], other_attributes=json.dumps(dict_line))
        mentor.save()


def handle_return_mentor_files(uploaded_file):
    data = convert_to_dicts(uploaded_file)
    print(data)
