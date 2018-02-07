# First problem of the 4th homework
# A word ladder solution using a tree which is implemented with a Python dictionary: starting from the start word
# leaves are added until there are children. If the goal is found the procedure ends and the path from the start
# word to the goal word is given.

import json
import os, sys
from collections import deque


def load_words():
    try:
        path = os.path.dirname(os.path.realpath(__file__))
        filename = path + "\words_dictionary.json"
        with open(filename, "r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)


class EquivalentWords:

    def __init__(self, start, goal, english_words):
        self.start = start
        self.goal = goal
        self.english_words = english_words
        self.to_explore_words = deque()
        self.neighbors = {}
    #conditions
        if self.start not in self.english_words:
            exit("Sorry, but the start word is not in the dictionary")
        if self.goal not in self.english_words:
            exit("Sorry, but the goal word is not in the dictionary")
        if self.goal == self.start:
            exit("The two words are equal, so there is no pathway between them")
        if len(self.start) != len(self.goal):
            exit("The two words have different lengths, so there is no pathway between them")

    def find_neighbors(self, word):
        self.neighbors[word] = []
        for j in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                newword = word[:j] + char + word[j + 1:]
                if newword in english_words:
                    self.neighbors[word].append(newword)
                    del english_words[newword]
        return self.neighbors[word]

    def find_previous(self, word):
        for previous in self.neighbors:
            if word in self.neighbors[previous]:
                return previous

    def find_pathway(self):
        # This adds the neighbors of start to the words that have to be explored
        del english_words[self.start]
        self.to_explore_words.extend(self.find_neighbors(self.start))
        # This part of the code checks each leaf: if the goal is found it exits; else it goes on adding leaves
        while self.to_explore_words:
            to_check_word = self.to_explore_words.popleft()
            if to_check_word == self.goal:
                break
            self.to_explore_words.extend(self.find_neighbors(to_check_word))

        reversedpathway = [self.goal]
        child = self.goal
        while child != self.start:
            parent = self.find_previous(child)
            if not parent:
                exit("Sorry, but there is no pathway between start and goal")
            else:
                reversedpathway.append(parent)
                child = parent
        pathway = reversedpathway[::-1]
        return pathway

english_words = load_words()
c = EquivalentWords("head", "tail", english_words)
print(c.find_pathway())

