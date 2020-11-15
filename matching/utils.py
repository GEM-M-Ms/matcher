import csv
import io

def convert_to_dicts(uploaded_file):
    file_bytes = uploaded_file.read().decode('utf-8')
    reader = csv.DictReader(io.StringIO(file_bytes))
    return [line for line in reader]

def handle_mentee_files(uploaded_file):
    data = convert_to_dicts(uploaded_file)
    print(data)


def handle_mentor_files(uploaded_file):
    convert_to_dicts(uploaded_file)
    print(data)


def handle_return_mentor_files(uploaded_file):
    convert_to_dicts(uploaded_file)
    print(data)
