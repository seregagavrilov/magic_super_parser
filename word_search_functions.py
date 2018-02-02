import ast

from exeptions import *

from nltk import pos_tag

import os

from service_functions import *


def serch_variables_names(asttrees, analyzepart):

    """
    :param asttrees: AST tree
    :param analyzepart: variables in AST trees
    :return:

    select variables in trees
    """

    variables = []

    for t in asttrees:
        for node in ast.walk(t):
            if isinstance(node, ast.FunctionDef):
                for nodefunction in ast.walk(node):
                    if isinstance(nodefunction, ast.Assign):
                        for nodeassign in ast.walk(nodefunction):
                            if isinstance(nodeassign, analyzepart) and not isinstance(nodeassign.ctx, ast.Load):
                                variables.append(nodeassign.id)

    return  variables


def search_functions_in_trees(asttrees, functionclass):
    """
    :param asttrees: all trees

    functionclass: class of objects to be found

    :return: python module trees

    select function module in trees function
    """
    functions = []

    for t in asttrees:
        for node in ast.walk(t):
            if isinstance(node, functionclass):
                functions.append(node.name.lower())

    if len(functions) == 0:

        raise FindInListError("The list is empty")

    return functions


def split_name_in_part_of_speech(parts):

    """
    :param functionsnames:

    :return: lists words

    split function name to words

    """

    splitdwords = []

    for word in parts:

        splitsname = word.split("_")

        splitdwords.append(splitsname)

    return splitdwords


def find_not_special_functions_in_tree(asttrees):

    sortedlist = leave_only_not_special_functions(asttrees)

    if len(sortedlist) == 0:

        raise FindInListError("The list is empty")

    return sortedlist


def leave_only_not_special_functions(listmodules):

    """
    :param listmodules: python modules

    :return: sort list without python magic function names

    The function selects not magic function names in the list
    """
    return [function for function in listmodules if not (function.startswith('__') and function.endswith('__'))]


def form_path_python_files(paths):
    """
    :param pathse: paths where we must find python files

    :return: python files

    """
    filesnames = []

    for path in paths:

        for root, dirs, files in os.walk(path, topdown=False):

            filesnames += [os.path.join(root, file) for file in files if file.endswith('.py')]

    if len(filesnames) == 0:

        raise FindInListError("The list is empty")

    return filesnames


def form_trees_ast(namessearch):

    """
    :param namessearch: name python files

    :return: AST trees

    Parse the source into an AST tree

    """

    asttrees = []

    for filename in namessearch:

        with open(filename, 'r', encoding='utf-8') as attempthandler:

            main_file_content = attempthandler.read()

        try:

            tree = ast.parse(main_file_content)

        except SyntaxError:

            continue

        asttrees.append(tree)

    return asttrees


def check_part_of_speech(wordcheck, part):
    """
    :param wordcheck: words that need to be check for part of the спечь
    :param part:чать речи на которую требуется проверить слово
    :return:

    Verification of a word on a part speech
    """

    if  part is None:

        raise PartSpeechError("Parameter part of speech is not specified")

    return pos_tag([wordcheck])[0][1] == part


def search_part_of_speech(wordfrommodul, part):
    """
    :param wordfrommodul: words that need to be check for part of the speech
            part: speech for which you want to test the word
    :return:list of matching words

    """

    names = list(filter(lambda x: len(x)> 0, add_values(wordfrommodul)))

    listword = []

    for name in names:

        if check_part_of_speech(name, part):
            listword.append(name)

    return listword