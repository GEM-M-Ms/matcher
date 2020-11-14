import csv

def handle_upload_files(f):

    with open(f) as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
