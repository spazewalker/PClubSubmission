#!/usr/bin/env python3

import csv
import json
import argparse

parser = argparse.ArgumentParser(description="check for the students selected in GSoC from IIT Kanpur", epilog="This script works only properly for this given format of data")
parser.add_argument("--csv",'-c' , nargs='?', default='gsoc_data.csv', help="Name of the CSV file of scrapped data from GSoC site(default: 'gsoc_data.csv')")
parser.add_argument("--json", '-j', nargs='?', default='students.json', help="Name of the JSON file containing the student data of IIT Kanpur(default: 'students.json')")
args = vars(parser.parse_args())

csv_file = args['csv']
json_file = args['json']


def populate_data(file,flag):
    if flag == 'csv':
        student_list = []
        with open(file, 'r') as readFile:
            reader = csv.DictReader(readFile)
            for row in reader:
                name = row['Name']
                if name != 'Name':
                    if not name.isspace():
                        if row['Name'].isupper:
                            if name.replace(' ','').isalpha():
                                student_list.append(row)
                                # print(row['Name'])
        return student_list
    if flag == 'json':
        with open(file,'r') as readFile:
            student_list = json.load(readFile)
        return student_list


def compare_and_print(gsoc,clg):
    for student in gsoc:
        for i in range(len(clg)):
            if clg[i]['n'] == student['Name']:
                name = student['Name']
                roll = clg[i]['i']
                branch = clg[i]['d']
                organisation = student['Organisation']
                project = student['Project']
                print(name,', ',roll,', ',branch,', ',organisation,', ',project)
                break

gsoc = populate_data(csv_file,'csv')
clg = populate_data(json_file,'json')
compare_and_print(gsoc,clg)



# Conditions on the name in csv file
# 1) The name contains any of the special symbols or numbers.
# 2) The name consists of only one word.
# 30 The name contains only lowercase letters.