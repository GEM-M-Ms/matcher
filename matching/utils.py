import csv
import io
import json
from .models import Mentor
from .models import Mentee
import numpy as np
import re

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from sortedcontainers import SortedList


def convert_to_dicts(uploaded_file):
    file_bytes = uploaded_file.read().decode("utf-8")
    reader = csv.DictReader(io.StringIO(file_bytes))
    return [line for line in reader]


def handle_mentee_files(uploaded_file):
    data = convert_to_dicts(uploaded_file)

    for row in data:
        name = f"{row['First Name']} {row['Last Name']}"
        email = row["Email Address"]
        attributes = {}

        for key, value in row.items():
            if re.search(r"\d", key):
                numberless_key = re.sub(" \d+", "", key)
                attr_array = attributes.get(numberless_key, [])
                if value:
                    attr_array.append(value)
                attributes[numberless_key] = attr_array
            else:
                attributes[key] = value
        mentee = Mentee(name=name, email=email, other_attributes=attributes)
        mentee.save()


def handle_mentor_files(uploaded_file):
    data = convert_to_dicts(uploaded_file)
    for dict_line in data:
        mentor = Mentor(
            name=dict_line["First Name"] + " " + dict_line["Last Name"],
            email=dict_line["Personal Email Address"],
            other_attributes=json.dumps(dict_line),
        )
        mentor.save()

    match_mentor(mentor)


def handle_return_mentor_files(uploaded_file):
    data = convert_to_dicts(uploaded_file)
    print(data)


def match_mentor(m):
    w1 = "Racial Discrimination"
    min_ratio=0

    y = json.loads(m.other_attributes)
    sw1 = y[w1]

    l = SortedList()
    for mr in Mentor.objects.all():
        jsonString = mr.other_attributes
        print("=================")
        print(mr.email)
        z = json.loads(jsonString)
        zw1 = z[w1]
        print(sw1)
        print(zw1)
        ratio=fuzz.ratio(sw1,zw1)
        print(ratio)
        if ratio > min_ratio:
            min_ratio = ratio
            #sortedcontainers insertion sort works in O(log n)
            #add to container {ratio,mentor}
            l.add(ratio,mr)

