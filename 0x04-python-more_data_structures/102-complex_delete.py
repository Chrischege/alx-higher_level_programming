#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    '''deletes a key:value pair from a given value'''
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return (a_dictionary)
