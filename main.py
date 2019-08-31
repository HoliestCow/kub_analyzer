
import numpy as np
import matplotlib.pyplot as plt
import glob
import kub_parser


def main():
    electric_target_string = './input/2019/*ELECTRIC*.csv'
    water_target_string = './input/2019/*WATER*.csv'
    electric_filelist = glob.glob(electric_target_string)
    water_filelist = glob.glob(water_target_string)

    consumption_dict = {'electricity': {}, 'water': {}}

    for bill in electric_filelist:
        billing_period = kub_parser.get_billing_period(bill)
        current_dict = kub_parser.parse(bill)
        consumption_dict['electricity'][billing_period] = current_dict
    for bill in water_filelist:
        billing_period = kub_parser.get_billing_period(bill)
        current_dict = kub_parser.parse(bill)
        consumption_dict['water'][billing_period] = current_dict
    return

main()
