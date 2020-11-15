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

    for line in data:
        create_and_save_mentor(line)




def handle_return_mentor_files(uploaded_file):
    data = convert_to_dicts(uploaded_file)
    print(data)

def get_json(name,l):
    s="{\""+name+"\":\""+json.dumps(l) + "}"
    print(s)
    return s

def  create_and_save_mentor(line):
    name=line["First Name"] + " " + line["Last Name"]
    career = line["Current Industry"]
    education = line["Alma Mater University/College"]
    area = line["City/Town in the GTA (Toronto, Durham, Peel, Halton, York)"]

    mentor = Mentor(name=line["First Name"] + " " + line["Last Name"], email=line["Personal Email Address"], other_attributes=json.dumps(line))
    mentor.career=career
    mentor.education=education
    mentor.area=area
    l=[line["Christianity"],line["Islam"],line["Hinduism"],line["Buddhism"],line["Sikhism"],line["Judaism"]]
    mentor.religius_identity=get_json("religius_identity",l)
    l=[line["Outgoing"],["Entrepreneurial"],line["Introverted"],line["Imaginative"],line["Competitive"],line["Team player"],line["Creative"],line["Logical"],line["Leader"],line["Detail oriented"],line["Spontaneous"],line["Patient"],line["Practical"],line["Empathetic"],line["Independent"]]
    mentor.personality=get_json("personality",line)
    l=[line["Playing Sports"],line["Watching Sports"],line["Volunteering"],line["Physical Activity"],line["Shopping"],line["Listening to Podcasts"],line["Listening to Music"],line["Playing Music"],line["Travelling"],line["Reading"],line["Spending Time With Family"],line["Spending Time With Friends"],line["Spending Time With Pets/Animals"],line["Visiting Museums/Art Galleries"],line["Cooking"],line["Learning New Things"],line["Going to Concerts"],line["Gardening"],line["Drawing and Visual Arts"],line["Camping/Spending Time Outdoors"]]
    mentor.hobbies=get_json("hobbies",l)
    mentor.save()


