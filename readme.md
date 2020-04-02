# Web Scrapper (Submission for PClub)

## How to run script:

### Install all dependencies
* Make a folder and clone this repo in it
* install dependencies

```
mkdir scrape
cd scrape
git clone https://github.com/spazewalker/PClubSubmission.git
pip3 install -r requirements.txt
```

### Using scrape.py
scrape.py can be use as it is for using default links and file names or
some arguments can be passed using -i or -o

```
$ python3 scrape.py -h
usage: scrape.py [-h] [--input [INPUT]] [--output [OUTPUT]]

scrape a particular webpage

optional arguments:
  -h, --help            show this help message and exit
  --input [INPUT], -i [INPUT]
                        Specify the link to extract data from(default='https:/
                        /summerofcode.withgoogle.com/archive/2019/projects/')
  --output [OUTPUT], -o [OUTPUT]
                        Specify the output csv file to write the
                        output(default='gsoc_data.csv')

This script works only properly for the given webpage
```

To use it with the defaults:

```
$ python3 scrape.py
```

### Using nameCheck.py
nameCheck is the script to check the names against the given condition and then printing the data for the students selected in GSoC on the stdout.


```
$ python3 nameCheck.py -h
usage: nameCheck.py [-h] [--csv [CSV]] [--json [JSON]]

check for the students selected in GSoC from IIT Kanpur

optional arguments:
  -h, --help            show this help message and exit
  --csv [CSV], -c [CSV]
                        Name of the CSV file of scrapped data from GSoC
                        site(default: 'gsoc_data.csv')
  --json [JSON], -j [JSON]
                        Name of the JSON file containing the student data of
                        IIT Kanpur(default: 'students.json')

This script works only properly for this given format of data
```

To use it with defaults:
```
$ python3 nameCheck.py
```

NOTE:
>Since students.json contains sensetive data. i'm not uploding it to github