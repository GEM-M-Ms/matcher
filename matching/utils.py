import csv
import io
import re

from .models import Mentee

def convert_to_dicts(uploaded_file):
    file_bytes = uploaded_file.read().decode('utf-8')
    reader = csv.DictReader(io.StringIO(file_bytes))
    return [line for line in reader]

def handle_mentee_files(uploaded_file):
    data = convert_to_dicts(uploaded_file)

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
        mentee = Mentee(name=name, email=email, other_attributes=attributes)
        mentee.save()

def handle_mentor_files(uploaded_file):
    convert_to_dicts(uploaded_file)
    print(data)


def handle_return_mentor_files(uploaded_file):
    convert_to_dicts(uploaded_file)
    print(data)
