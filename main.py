
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

    for bill in electric_filelist:
        billing_period = kub_parser.get_billing_period(bill)
        current_dataframe = kub_parser.parse(bill)
        current_dataframe.columns = ['time', 'electricity_consumption']
        master_dataframe += [current_dataframe]
    master_dataframe = pd.concat(master_dataframe, ignore_index=True)
    print(master_dataframe)

    # NOTE: Figure out this merging stuff. 
    for bill in water_filelist:
        billing_period = kub_parser.get_billing_period(bill)
        current_dataframe = kub_parser.parse(bill)
        current_dataframe.columns = ['time', 'water_consumption']
        master_dataframe = pd.merge(master_dataframe, current_dataframe,
                                    on='time')
    return

main()
