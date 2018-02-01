# First problem of the 4th homework
# A word ladder solution using a tree which is implemented with a Python dictionary: starting from the start word
# leaves are added until there are children. If the goal is found the procedure ends and the path from the start
# word to the goal word is given.

import json
import os, sys
from collections import deque

# The dictionary is read
def load_words():
    try:
        path = os.path.dirname(os.path.realpath(__file__))
        filename = path + "\words_dictionary.json"
        with open(filename,"r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)


# This function finds the neighbors of a word, i.e. the words that differ from a word by a character
def find_neighbors(word):
    neighbors[word] = []
    for j in range(len(word)):
        for char in alphabet:
            newword = word[:j] + char + word[j+1:]
            if newword in list_dictionary and newword not in explored_words and newword not in to_explore_words:
                neighbors[word].append(newword)
    return neighbors[word]

# This function finds a word starting from one of its neighbors
def find_previous(word):
    for previous in neighbors:
        if word in neighbors[previous]:
            return previous

# Definitions
english_words = load_words()
start = "head"
goal = "tail"
alphabet = "abcdefghijklmnopqrstuvwxyz"
explored_words = [start]
to_explore_words = deque()
neighbors = {}

# This part of the code checks for special cases
if start not in english_words:
    exit("Sorry, but the start word is not in the dictionary")
if goal not in english_words:
    exit("Sorry, but the goal word is not in the dictionary")
if goal == start:
    exit("The two words are equal, so there is no pathway between them")
if len(start) != len(goal):
    exit("The two words have different lengths, so there is no pathway between them")

# A list of words which are as long as start is created
list_dictionary = []
for i in english_words:
    if len(i) == len(start):
        list_dictionary += [i]

# This adds the neighbors of start to the words that have to be explored
to_explore_words.extend(find_neighbors(start))

# This part of the code checks each leaf: if the goal is found it exits; else it goes on adding leaves
while to_explore_words:
    to_check_word = to_explore_words.popleft()
    print(to_check_word)
    if to_check_word == goal:
        break
    explored_words.append(to_check_word)
    to_explore_words.extend(find_neighbors(to_check_word))

# Here the pathway is found starting from the goal and going back to the start
reversedpathway = [goal]
child = goal
while child != start:
    parent = find_previous(child)
    if not parent:
        exit("Sorry, but there is no pathway between start and goal")
    else:
        reversedpathway.append(parent)
        child = parent
pathway = reversedpathway[::-1]
print(pathway)
