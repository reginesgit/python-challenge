# Script for PyBank analysis

import os
import csv

# PyBank\Resources\budget_data.csv
filepath = os.path.join('..', 'Resources', 'budget_data.csv').replace("\\","/")

with open(filepath) as csvfile:

    filereader = csv.reader(filepath, delimiter=',')

    print(filepath)