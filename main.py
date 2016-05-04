from Pal import get_palindromes
import argparse

def println(string):
    print(string)

parser = argparse.ArgumentParser()
parser.add_argument("dictionary", help="dictionary file to read, line separated")
parser.add_argument("length", help="maximum palindrome length", type=int)
args = parser.parse_args()

get_palindromes(args.dictionary, args.length, println, '[a-z]+$')
