#!/usr/bin/python3
"""Check if an object is exactly an instance of a given class."""

def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """

    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
