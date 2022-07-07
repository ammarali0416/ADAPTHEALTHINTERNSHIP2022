# AUTHOR: Ammar Syed Ali
# DATE: 7/5/2022
# TITLE: NPPES API
########################
########################
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Importing Libraries
import requests
import json
import pandas as pd
import numpy as np
from flatten_json import flatten, flatten_json
from random import randint

# List of  NPI
NPI_list = [
    1164731923,
    1629445267,
    1437168713,
    1033118161,
    1962815308,
    1235393059,
    1023410586,
    1568816288,
    1841262938,
    1700070224
]

print(NPI_list)

# JSON request from NPI registry
# r = requests.get(
#    'https://npiregistry.cms.hhs.gov/api/'
#    '?number=&'
#    'enumeration_type=&'
#    'taxonomy_description=&'
#    'first_name=SEEMA&'
#    'last_name=NISHAT&'
#    'organization_name=&'
#    'address_purpose=&'
#    'city=&'
#    'state=&'
#    'postal_code=&'
#    'country_code=&'
#    'limit=10&'
#    'skip=&'
#    'version=2.0'
#    )
# results_text = r.text
# print(results_text)
#
# Converting result into JSON object
# results_json = r.json()
# print(results_json['results'][0]['basic']['first_name'])
#
# Flatting the object and storing in dataframe
# record = flatten(results_json['results'][0])
# df1 = pd.DataFrame.from_dict(record,orient='index').T
# print(df1)

i = 0
while i < len(NPI_list):
    r = requests.get(
        'https://npiregistry.cms.hhs.gov/api/?number={0}&'
        'enumeration_type=&'
        'taxonomy_description=&'
        'first_name=&'
        'last_name=&'
        'organization_name=&'
        'address_purpose=&'
        'city=&'
        'state=&'
        'postal_code=&'
        'country_code=&'
        'limit=1&'
        'skip=&'
        'version=2.0'.format(NPI_list[i])
    )
    print(r.text)  # In unusable format
    json_usable = r.json()  # Converts JSON to nested dictionary
    record = flatten(json_usable['results'][0])  # Selects the [0] record the 'results' dictionary from json_usable and
    # flattens it#
    data = pd.DataFrame.from_dict(record, orient='index').T
    if i == 0:
        df1 = data
    else:
        df1 = pd.concat([df1, data], axis=0, ignore_index=True)
    i += 1

df1.to_csv('NPI_Export.csv')

#added comment