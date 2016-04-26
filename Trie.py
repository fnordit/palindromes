from itertools import *

class Trie:
    def __init__(self, tail = "", head = ""):
        self.letter = head
        self.term = False
        self.children = {}
        self.insert(tail)

    def insert(self, word):
        if len(word) == 0:
            if self.letter != "":
                self.term = True
            return
        head = word[0]
        tail = word[1:]
        try:
            self.children[head].insert(tail)
        except KeyError:
            self.children[head] = Trie(tail, head)

    def output(self, depth = 0):
        out = ""
        for i in range(depth):
            out += "|"
        out += self.letter
        if self.term:
            out += "*"
        print(out)
        for c in self.children.values():
            c.output(depth+1)

    def find_words(self, word = ""):
        current = word + self.letter
        word_list = []
        if self.term:
            word_list += [current]
        for c in self.children.values():
            word_list += c.find_words(current)
        return word_list

    def find_pref(self, prefix):
        if len(prefix) == 0:
            return self
        head = prefix[0]
        tail = prefix[1:]
        try:
            return self.children[head].find_pref(tail)
        except KeyError:
            return None

    def find_from_pref(self, prefix):
        root = self.find_pref(prefix)
        if root == None or root.children.values() == []:
            return []
        return reduce(lambda x,y: x+y, [c.find_words() for c in root.children.values()])

    def is_word(self, word):
        return self.find_pref(word) and self.find_pref(word).term
