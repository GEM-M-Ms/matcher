import csv
import json
from .models import Mentor


def handle_upload_files(f):

    for chunk in f.chunks():
        print(chunk)

def handle_file(variables_file):

    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs

    reader = csv.DictReader(open(variables_file, 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)

    for dict_line in dict_list:
        print(dict_line["Personal Email Address"])
        mentor = Mentor(name=dict_line["First Name"] + " " + dict_line["Last Name"], email=dict_line["Personal Email Address"], other_attributes={})
        mentor.save()


def handle_mentee_files(f):
    handle_upload_files(f)


def handle_mentor_files(f):
    handle_upload_files(f)
    handle_file("mentor.csv")


def handle_return_mentor_files(f):
    handle_upload_files(f)
