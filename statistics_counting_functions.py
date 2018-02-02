import collections

def extract_most_used_functions(listofwords):

    return {word: count for word, count in collections.Counter(listofwords).most_common(200)}
