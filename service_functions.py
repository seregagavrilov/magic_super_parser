import git

from git import Repo

import json

import csv


def add_values(somelist):

    """
    :param somelist:

    :return:  [(1,2), (3,4)] -> [1, 2, 3, 4]

    """
    return sum([list(item) for item in somelist], [])


def clone_repository(where_from, to_path):
    """

    :param where_from:URL from where you need to clone
    :param to_path:the path to be clone

    Clone repository to path
    """

    return Repo.clone_from(where_from, to_path).working_dir


def create_a_parameter_dictionary(parameters):

    """
    :param parameters: list if paramiters
    :return: dict parameters

    creates a dictionary of program parameters
    """
    dictparameters = {}

    for i in parameters:

        t = i.split(",")

    index = 0

    while index < len(t):

        if t[index] != '':
            dictparameters['paramiternomber_' + str(index+1)] = t[index]
        else:
            dictparameters['paramiternomber_' + str(index+1)] = None

        index = index + 1

    return dictparameters


def show_the_result_of_counting_words(words):

    for word, occurrence in words.items():

        print(word, occurrence)


def save_in_file(formatfile, mostcommonwords):
    """
    :param formatfile: format which you need to dave the file
    :param mostcommonwords: dict words words and number of uses

    """

    if len(mostcommonwords) == 0:

        return None

    if formatfile == "JSON":

        with open('json.txt', 'a') as file:

            json.dump(mostcommonwords, file,sort_keys = True)

    elif formatfile == "CSV":

        with open('csv.csv', 'a') as file:

            writer = csv.writer(file)

            for word, count in mostcommonwords.items():

                writer.writerow([word, count])
