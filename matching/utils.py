import csv
import io
import json
from .models import Mentor
from .models import Mentee
import numpy as np

def convert_to_dicts(uploaded_file):
    file_bytes = uploaded_file.read().decode('utf-8')
    reader = csv.DictReader(io.StringIO(file_bytes))
    return [line for line in reader]

def handle_mentee_files(uploaded_file):
    data = convert_to_dicts(uploaded_file)
    print(data)


def handle_mentor_files(uploaded_file):
    data  = convert_to_dicts(uploaded_file)
    for dict_line in data:
        mentor = Mentor(name=dict_line["First Name"] + " " + dict_line["Last Name"], email=dict_line["Personal Email Address"], other_attributes=json.dumps(dict_line))
        mentor.save()

    match_mentor(mentor)

def handle_return_mentor_files(uploaded_file):
    data = convert_to_dicts(uploaded_file)
    print(data)


def match_mentor(m):
    w1 = "Career Interest"
    
    y = json.loads(m.other_attributes)
    sw1=y[w1]
    sw2=y[w2]
    sw3=y[w3]
    sw4=y[w4]
    sw5=y[w5]
    sw6=y[w6]

    for mr in Mentor.objects.all():
        jsonString = mr.other_attributes
        print("=================")
        print(mr.email)
        z = json.loads(jsonString)
        print(y)
        zw1=z[w1]


        print(sw1.contains(yz[w1]))
        Str1 = sw1
        Str2 = yz[w1]
        Distance = levenshtein_ratio_and_distance(Str1.lower(),Str2.lower())
        print(Distance)
        Ratio = levenshtein_ratio_and_distance(Str1.lower(),Str2.lower(),ratio_calc = True)
        print(Ratio)

def levenshtein_ratio_and_distance(s, t, ratio_calc = False):
      """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
  # Initialize matrix of zeros
          rows = len(s)+1
          cols = len(t)+1
          distance = np.zeros((rows,cols),dtype = int)

  # Populate matrix of zeros with the indeces of each character of both strings
          for i in range(1, rows):
              for k in range(1,cols):
                  distance[i][0] = i
                  distance[0][k] = k

  # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions
          for col in range(1, cols):
              for row in range(1, rows):
                  if s[row-1] == t[col-1]:
                      cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
                  else:
                      # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                      # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                      if ratio_calc == True:
                          cost = 2
                      else:
                          cost = 1
                  distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                  distance[row][col-1] + 1,          # Cost of insertions
                  distance[row-1][col-1] + cost)     # Cost of substitutions
          if ratio_calc == True:
            # Computation of the Levenshtein Distance Ratio
              Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
              return Ratio
          else:
            # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
            # insertions and/or substitutions
            # This is the minimum number of edits needed to convert string a to string b
              return "The strings are {} edits away".format(distance[row][col])
