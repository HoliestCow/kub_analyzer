
import csv
import datetime
import pandas as pd

def parse(inputfilename):

    time = []
    value = []

    with open(inputfilename) as csvfile:
        doc = csv.reader(csvfile)
        next(doc)
        for row in doc:
            timedate = row[0]  # day month year hour:minute
            datetime_obj = datetime.datetime.strptime(timedate, '%d %b %Y %H:%M')
            usage = row[1]  #kwH
            if usage == '':
                usage = 0.0
            else:
                usage = float(usage)
            time += [datetime_obj]
            value += [usage]
    out_dict = {'time': time, 'consumption': value}
    data = pd.DataFrame(data=out_dict, columns=['time', 'consumption'])
    return data

def get_billing_period(inputfilename):
    two_cities = inputfilename.split('-')
    sandwich = two_cities[-1]
    month_string = sandwich[:4]
    return month_string
