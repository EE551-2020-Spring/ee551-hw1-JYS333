#!/usr/bin/python

"""
Python Core object Types
"""

import math

def numbers_and_strings():
    """
    This is to review numbers and strings and basic operations.
    """
    # Assign a string "EE551" to a variable x
    x = "EE551"

    # Assign a string "Stevens" to a variable y
    y = "Stevens"

    # Repeat variable y 5 times
    z = y*5

    # What is the length of z?
    length = len(z)

    # Concatenate variable y with string " is good"
    m = y + " is good"

    # Replace "good" with "awesome" in variable m and assign it to a new variable n
    n = m.replace("good", "awesome")

    # print(x, y, z, length, m, n)
    return x, y, z, length, m, n



def lists():
    """
    This is to review basic operations with lists.
    """
    n = "Stevens is awesome"

    # Split variable n on a delimiter space into a list of substrings
    p = n.split(" ")

    # Get all the items past the first of the third substring
    r = []
    for i in p:
        r += i[:1]

    # Create a 3 x 3 matrix as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]
    c = [[1, 4, 5],[6, 10, 11],[12, 17, 38]]
    d = []
    # Collect the items in the last column of matrix A using list comprehension
    for i in c:
        d += i[2:]

    # Collect only the even items of the diagonal of matrix A using list comprehension
    o = []
    for i in c:
        for j in i:
            if j % 2 == 0:
                o.append(j)

    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "Stevens" using list comprehension.

    # print(p, r, c, d, o)
    return p, r, c, d, o


def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 4
    #   color => "green"
    f = {
        'fruit': 'apple',
        'quantity': 4,
        'color': 'green'
    }

    # Get the item in dictionary f that the key "fruit" maps to
    a = f['fruit']

    # Increase the quantity of f by 1
    # IMPLEMENT IT HERE
    f['quantity'] += 1

    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85
    nDic = {
        'name': {'first_name': 'Grace', 'last_name': 'Hopper'},
        'jobs': ['scientist', 'engineer'],
        'age': 85
    }

    # Add "programmer" to the list of jobs Grace has
    # IMPLEMENT IT HERE
    nDic['jobs'].append('programmer')

    # Get the third job Grace has that you recently added
    p = nDic['jobs'][2]

    # Use the sort() function to get sorted keys of amazing_grace in alphabetically ascending order
    k = sorted(nDic)

    # print(a, f, p, k)
    return a, f, p, k

numbers_and_strings()
lists()
dictionaries()
