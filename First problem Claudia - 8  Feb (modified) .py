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
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.tree = {}
        self.msg = ""
        if type(self.english_words) == str:
            self.msg = "Sorry, the dictionary cannot be found: " + english_words
        elif start not in english_words:
            self.msg = "Sorry, but the start word is not in the dictionary"
        elif goal not in english_words:
            self.msg = "Sorry, but the goal word is not in the dictionary"
        elif goal == start:
            self.msg = "The two words are equal, so there is no pathway between them"
        elif len(start) != len(goal):
            self.msg = "The two words have different lengths, so there is no pathway between them"
        else:
            self.build_tree()
            self.msg = self.find_path()

    def build_tree(self):
        goalfound = False
        to_explore_words = deque()
        to_explore_words.append(self.start)
        del english_words[self.start]
        while to_explore_words and not goalfound:
            to_check_word = to_explore_words.popleft()
            if to_check_word == self.goal:
                goalfound = True
            else:
                self.tree[to_check_word] = self.find_neighbors(to_check_word)
                to_explore_words.extend(self.tree[to_check_word])
        if not goalfound:
            self.tree.clear()
        return self.tree

    def find_neighbors(self, word):
        neighbors = []
        for j in range(len(word)):
            for char in self.alphabet:
                newword = word[:j] + char + word[j + 1:]
                if newword in english_words:
                    neighbors.append(newword)
                    del english_words[newword]
        return neighbors

    def find_path(self):
        if self.tree.get(self.start):
            reversedpathway = [self.goal]
            child = self.goal
            while child != self.start:
                parent = self.find_previous(child)
                reversedpathway.append(parent)
                child = parent
            pathway = reversedpathway[::-1]
            msg = ""
            for i in pathway:
                msg += i + " "
        else:
            msg = "Sorry, but there is no pathway between start and goal"
        return msg

    def find_previous(self,word):
        for previous in self.tree:
            if word in self.tree[previous]:
                return previous


english_words = load_words()
c = EquivalentWords("begin", "house", english_words)
print(c.msg)
