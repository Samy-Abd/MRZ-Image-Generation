from mrz.generator.td1 import TD1CodeGenerator
import mrz
import numpy as np
from tqdm import tqdm
import random
from datetime import date, timedelta
import string
def generate_random_date():
    start_date = date(1900, 1, 1)  # Start date
    end_date = date(2100, 12, 31)  # End date
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime("%y%m%d")  # Format the date as YYMMDD


def generate_random_alphanum(length=9):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choices(letters_and_digits, k=length))

names = []
with open('data/sample.txt', 'r') as f_nom:
    for line in tqdm(f_nom):
        names.append(line.replace('\n', ""))

mrz_list = []
sex = 'F'
cpt = 0
with open('data/mrz.txt', 'w') as f_in:
    for i in names:
        i = i.split('|')
        if len(i[0])+len(i[1]) >= 30:
            continue
        res = TD1CodeGenerator(       "ID",
                                "DZA",
                                generate_random_alphanum(),
                                generate_random_date(),
                                sex,
                                generate_random_date(),
                                "DZA",
                                i[0], 
                                i[1],
                                "")
        if sex == 'F':
            sex = 'M'
        else:
            sex = 'F'
        cpt += 1
        f_in.write(str(res))
        f_in.write('\n\n')
        if cpt == 5000:
            break