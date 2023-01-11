"""
Contains the logic for randomly creating

"""

import re
from random import choice
from random import randint
from pathlib import Path

path = Path(__file__).parent.absolute()
male_path = str(path) + r"/data/dist.male.first"
female_path = str(path) + r"/data/dist.female.first"
surname_path = str(path) + r"/data/dist.all.last"

def array_from_file(filepath):
    """
    Reads in the dat file containing data
    and store the first column into a lista
    :return: A list of data
    """
    array_data = []
    with open(filepath, 'r') as data:
        for x in data:
            res = ''.join(re.findall('[a-zA-Z]+', x))
            array_data.append(res)
    return array_data

def male_first_name(male_names):
    """
    Reads in the array containing male
    names and returns a random
    male name.
    :return: A random male first name
    """
    random_male = choice(male_names)
    return random_male.capitalize()


if __name__ == '__main__':
    male_names = array_from_file(male_path)