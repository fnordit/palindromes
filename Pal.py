from Trie import *
import re
import sys

def reverse(string):
    return string[::-1]

def is_palindrome(word):
    return word == reverse(word)

def get_palindromes(filename, length, function, regex):
    def generate(root, remainder, front, depth):
        if depth <= 0:
            return
        if remainder == "":
            function(root)
            return
        if front:
            # [                     root | remainder]
            # [merwen | redniamer + root + remainder]
            candidates = backward.find_from_pref(remainder)
            for danc in candidates:
                newroot = reverse(danc) + reverse(remainder) + " " + root
                generate(newroot, danc, False, depth-1)
            # [      root | remainder   ]
            # [mer + root + rem | ainder]
            for i in range(len(remainder)+1):
                if backward.is_word(remainder[0:i]):
                    newroot = reverse(remainder[0:i]) + " " + root 
                    newrem = remainder[i:]
                    generate(newroot, newrem, True, depth-1)
        else:
            # [remainder | root]
            # [remainder + root + redniamder | newrem]
            candidates = forward.find_from_pref(remainder)
            for cand in candidates:
                newroot = root + " " + remainder + cand
                generate(newroot, cand, True, depth-1)
            # [remainder    | root      ]
            # [remain | der + root + red]
            for i in range(1,len(remainder)+1):
                if forward.is_word(remainder[0:i]):
                    newroot = root + " " + remainder[0:i]
                    newrem = remainder[i:]
                    generate(newroot, newrem, False, depth-1)
        return

    try:
        dictionary = open(filename, 'r')
    except:
        print "Error: invalid dict file."
        sys.exit()

    forward = Trie()
    backward = Trie()
    for word in dictionary:
        if re.compile(regex).match(word):
            forward.insert(word.strip())
            backward.insert(word[::-1].strip())
    dictionary.close()

    for word in forward.find_words():
        for i in range(len(word)):
            if is_palindrome(word[0:i]):
                generate(word, word[i:], True, length)
        for i in reversed(range(len(word))):
            if is_palindrome(word[i:]):
                generate(word, reverse(word[0:i]), False, length)
