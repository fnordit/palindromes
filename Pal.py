from Trie import *
import re
import argparse
import sys

def is_palindrome(word):
    return word == word[::-1]

def get_palindromes(root, remainder, front, depth):
    if depth <= 0:
        return
    if remainder == "":
        print root
        return
    ret = []
    if front:
        # [                     root | remainder]
        # [merwen | redniamer + root + remainder]
        candidates = backward.find_from_pref(remainder)
        #print(str(depth) + "FRONT\tRoot: " + root + "\tRemainder: " + remainder)
        #print(candidates)
        for danc in candidates:
            newroot = danc[::-1] + remainder[::-1] + " " + root
            get_palindromes(newroot, danc, False, depth-1)
        # [      root | remainder   ]
        # [mer + root + rem | ainder]
        for i in range(len(remainder)+1):
            if backward.is_word(remainder[0:i]):
                newroot = remainder[0:i][::-1] + " " + root 
                newrem = remainder[i:]
                get_palindromes(newroot, newrem, True, depth-1)
    else:
        # [remainder | root]
        # [remainder + root + redniamder | newrem]
        candidates = forward.find_from_pref(remainder)
        #print(str(depth) + "BACK\tRoot: " + root + "\tRemainder: " + remainder)
        #print(candidates)
        for cand in candidates:
            newroot = root + " " + remainder + cand
            get_palindromes(newroot, cand, True, depth-1)
        # [remainder    | root      ]
        # [remain | der + root + red]
        for i in range(1,len(remainder)+1):
            if forward.is_word(remainder[0:i]):
                newroot = root + " " + remainder[0:i]
                newrem = remainder[i:]
                get_palindromes(newroot, newrem, False, depth-1)
    return

parser = argparse.ArgumentParser()
parser.add_argument("dictionary", help="dictionary file to read, line separated")
parser.add_argument("length", help="dictionary file to read, line separated", type=int)
args = parser.parse_args()
try:
    dictionary = open(args.dictionary, 'r')
except:
    print "Error: invalid dict file."
    sys.exit()
forward = Trie()
backward = Trie()
for word in dictionary:
    if re.compile('[a-z]+$').match(word):
        forward.insert(word.strip())
        backward.insert(word[::-1].strip())

for word in forward.find_words():
    for i in range(len(word)):
        if is_palindrome(word[0:i]):
            get_palindromes(word, word[i:], True, args.length)
    for i in reversed(range(len(word))):
        if is_palindrome(word[i:]):
            get_palindromes(word, word[0:i][::-1], False, args.length)
