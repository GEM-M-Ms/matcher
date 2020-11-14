import csv


def handle_upload_files(f):

    for chunk in f.chunks():
        print(chunk)


def handle_mentee_files(f):
    handle_upload_files(f)


def handle_mentor_files(f):
    handle_upload_files(f)


def handle_return_mentor_files(f):
    handle_upload_files(f)
