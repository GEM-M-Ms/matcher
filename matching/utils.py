import csv

def handle_upload_files(f):

    for chunk in f.chunks():
        print(chunk)

