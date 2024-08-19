# Author: Khrystian Clark
# Date: 2/25/2020
# Description:  This program takes two statements and gives the user back the words in each that match and nothing else.

"""Defines the function to be dealt and the two statements"""
def words_in_both(s1, s2):
  """splits each statement into sets and takes the intersects of both sets"""
  return {i for i in s1.split() if i in s2.split()}