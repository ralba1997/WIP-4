# Second problem of the 4th homework
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


# This function finds the neighbors of a word, i.e. the words that differ from a word by a character (substituted,
# deleted or added)
def find_neighbors(aword):
    neighbors = []
    for j in range(len(aword)):
        for char in alphabet:
            newword = aword[:j] + char + aword[j+1:]
            if newword in english_words:
                neighbors.append(newword)
                del english_words[newword]
    for j in range(len(aword)):
        newword = aword[:j] + aword[j+1:]
        if newword in english_words:
            neighbors.append(newword)
            del english_words[newword]
    for j in range(1, len(aword)):
        for char in alphabet:
            newword = aword[:j] + char + aword[j:]
            if newword in english_words:
                neighbors.append(newword)
                del english_words[newword]

    return neighbors

# This function finds a word starting from one of its neighbors
def find_previous(word):
    for previous in tree:
        if word in tree[previous]:
            return previous

# This adds the neighbors of start to the words that have to be explored
# This part of the code checks each leaf: if the goal is found it exits; else it goes on adding leaves

def build_tree():
    goalfound = False
    to_explore_words = deque()
    to_explore_words.append(start)
    del english_words[start]
    while to_explore_words and not goalfound:
        to_check_word = to_explore_words.popleft()
        if to_check_word == goal:
            goalfound = True
        else:
            tree[to_check_word] = find_neighbors(to_check_word)
            to_explore_words.extend(tree[to_check_word])
    if not goalfound:
        tree.clear()
    return tree

# Here the pathway is found starting from the goal and going back to the start
def find_path(tree):
    if tree.get(start):
        reversedpathway = [goal]
        child = goal
        while child != start:
            parent = find_previous(child)
            reversedpathway.append(parent)
            child = parent
        pathway = reversedpathway[::-1]
        msg = ""
        for i in pathway:
            msg += i + " "
    else:
        msg = "Sorry, but there is no pathway between start and goal"
    return msg


# Definitions
english_words = load_words()
alphabet = "abcdefghijklmnopqrstuvwxyz"
start = "head"
goal = "tea"
tree = {}
msg = ""

# This part of the code checks for special cases
if type(english_words) == str:
    msg = "Sorry, the dictionary cannot be found:" + english_words
elif start not in english_words:
    msg = "Sorry, but the start word is not in the dictionary"
elif goal not in english_words:
    msg = "Sorry, but the goal word is not in the dictionary"
elif goal == start:
    msg = "The two words are equal, so there is no pathway between them"
else:
    tree = build_tree()
    msg = find_path(tree)
print(msg)
