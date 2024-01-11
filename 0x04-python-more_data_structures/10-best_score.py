#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    list_scores = list(a_dictionary.values())
    list_keys = list(a_dictionary.keys())
    max_score = max(list_scores)
    index_of_max = list_scores.index(max_score)
    return list_keys[index_of_max]
