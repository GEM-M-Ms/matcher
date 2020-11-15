import csv
import json
from .models import Mentor


def handle_upload_files(f):

    for chunk in f.chunks():
        print(chunk)
        for row in chunk:
            print(row)

        reader = csv.DictReader(open('mentor.csv', 'r'))
        dict_list = []
        for line in reader:
            dict_list.append(line)


        for lline in dict_list:
            mentor = Mentor(name=lline["First Name"] + " " + lline["Last Name"], email=lline["Personal Email Address"], other_attributes={})
            mentor.save()



def handle_mentee_files(f):
    handle_upload_files(f)


def handle_mentor_files(f):
    handle_upload_files(f)


def handle_return_mentor_files(f):
    handle_upload_files(f)
