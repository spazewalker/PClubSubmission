#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import re
import csv
import argparse


parser = argparse.ArgumentParser(description="scrape a particular webpage", epilog="This script works only properly for the given webpage")
parser.add_argument("--input",'-i', help="Specify the link to extract data from(default='https://summerofcode.withgoogle.com/archive/2019/projects/')", nargs='?', default='https://summerofcode.withgoogle.com/archive/2019/projects/')
parser.add_argument("--output", '-o', help="Specify the output csv file to write the output(default='gsoc_data.csv')", nargs='?', default='gsoc_data.csv')
args = vars(parser.parse_args())

base_link = 'https://summerofcode.withgoogle.com'
link =  args['input']
output = args['output']

def findAndSave(soup,output):
    cards = soup.find_all("div",re.compile("md-padding archive-project-card__header"))
    with open(output, 'a+') as file:
        fieldnames = ['Name','Project','Organisation']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for card in cards:
            name = card.a.get_text()
            project = card.select('div')[0].get_text()
            organisation = card.select('div')[1].get_text()
            organisation = organisation.replace('Organization: ','')
            # print('Name: ',name, 'Project: ',project,"Organisation: ", organisation)
            writer.writerow({'Name':name, 'Project': project, 'Organisation': organisation})
    return


def getSoup(link):
    print('Scrapping page with url: ',link)
    result = requests.get(link)
    if result.status_code != 200 :
        print("can't access the webpage")
    else:
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        return soup



soup = getSoup(link)
findAndSave(soup,output)
a = soup.find("a",string=re.compile('Next'))
val = input('Do you want to continue scrapping on the next pages? [y/n]:    ')
if val == 'y' or val == 'Y':
    while a:
        link = base_link + a['href']
        soup = getSoup(link)
        findAndSave(soup,output)
        a = soup.find("a",string=re.compile('Next'))