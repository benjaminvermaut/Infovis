import json, csv
import random


def mph_to_km(mph):
    """
        Convert Mph to Km/h
    :param mph: unit of speed to convert (float)
    :return: conversion of mph to km/h (float)
    """
    kmh = mph * 1.61
    return kmh

def get_infos_fossil(fossil):
    """
        Browse dinosaurs.csv and return the information corresponding to the fossil

    :param fossil: the fossil we want more information about (dict)
    :return: additional information on the fossil (list)
    """

    with open('dinosaurs.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            if line[0] in fossil['name'].lower():
                return line


def add_info_fossil(fossil):
    """
    :param fossil: the fossil we want to update (dict)
    :return: fossil updated with its additional information (dict)
    """

    additional_info = get_infos_fossil(fossil)
    fossil['zone'] = additional_info[1]
    fossil['diet'] = additional_info[2]
    size = additional_info[3].split(' ')
    weight = additional_info[4].split(' ')
    speed = additional_info[5].split(' ')
    # assigns a number within the size range
    if len(size) > 2:
        pseudo_random_size = random.uniform(float(size[0]), float(size[2]))
        rounded = round(pseudo_random_size, 1)
        fossil['size'] = rounded
    else:
        fossil['size'] = float(size[0])

    # assigns a number within the weight range
    if len(weight) > 2:
        pseudo_random_size = random.uniform(float(weight[0]), float(weight[2]))
        rounded = round(pseudo_random_size, 1)
        fossil['weight'] = rounded
    else:
        fossil['weight'] = float(weight[0])

    # assigns a number within the speed range
    if len(speed) > 2:
        pseudo_random_size = random.uniform(float(speed[0]), float(speed[2]))
        rounded = round(pseudo_random_size, 1)
        fossil['speed'] = rounded
        if speed[3] == 'mph':
            fossil['speed'] = round(mph_to_km(rounded), 1)
    else:
        fossil['speed'] = round(float(speed[0]), 1)
        if speed[1] == 'mph':
            fossil['speed'] = round(mph_to_km(float(speed[0])), 1)

    fossil['lived'] = additional_info[6]



if __name__ == '__main__':
    with open('fossils.json', encoding="utf8") as json_file:
        fossils = json.load(json_file)

    for fossil in fossils:
        # delete information we don't need in fossils dataset
        del fossil['rank'], fossil['early_interval'], fossil['late_interval'], fossil['country'], fossil['state'], \
            fossil['county'], fossil['comment'], fossil['formation'], fossil['lithology'], fossil[
            'lithology_description'], \
            fossil['old_latitude'], fossil['old_longitude'],

        # add information to complete fossils datasets
        add_info_fossil(fossil)

    # create our new dataset
    with open('new_fossils', 'w') as f:
        json.dump(fossils, f)

