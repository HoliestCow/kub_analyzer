
import numpy as np
import matplotlib.pyplot as plt
import glob
import kub_parser
import pandas as pd


def main():
    electric_target_string = './input/2019/*ELECTRIC*.csv'
    water_target_string = './input/2019/*WATER*.csv'
    electric_filelist = glob.glob(electric_target_string)
    water_filelist = glob.glob(water_target_string)

    # master_dataframe = pd.DataFrame(data=None, columns='time')
    master_dataframe = []
    electric_dataframe = []
    water_dataframe = []

    for bill in electric_filelist:
        billing_period = kub_parser.get_billing_period(bill)
        current_dataframe = kub_parser.parse(bill)
        current_dataframe.columns = ['time', 'electricity_consumption']
        electric_dataframe += [current_dataframe]

    # NOTE: Figure out this merging stuff. 
    for bill in water_filelist:
        print(bill)
        billing_period = kub_parser.get_billing_period(bill)
        current_dataframe = kub_parser.parse(bill)
        current_dataframe.columns = ['time', 'water_consumption']
        water_dataframe += [current_dataframe]

    electric_dataframe = pd.concat(electric_dataframe)
    electric_dataframe = electric_dataframe.set_index('time')
    water_dataframe = pd.concat(water_dataframe)
    water_dataframe = water_dataframe.set_index('time')

    master_dataframe = pd.merge(electric_dataframe, water_dataframe,
                                left_index=True, right_index=True)
    master_dataframe['year'] = master_dataframe.index.year
    master_dataframe['month'] = master_dataframe.index.month
    master_dataframe['weekday_name'] = master_dataframe.index.weekday_name
    master_dataframe['hour'] = master_dataframe.index.hour
    print(master_dataframe.sample(5, random_state=0))
    return

main()
