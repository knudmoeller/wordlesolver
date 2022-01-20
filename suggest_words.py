import argparse
import re

parser = argparse.ArgumentParser(
    description="Suggest solutions to Wordle based on some constraints.")
parser.add_argument('-d', '--dictionary',
                    default="/usr/share/dict/words",
                    help="Dictionary file to use as the starting point. Default is '/usr/share/dict/words'.")
parser.add_argument('-p', '--present',
                    default="",
                    help="All letters that we know are in the word, all in one string. Default is '' (emtpy string).")
parser.add_argument('-n', '--not-present',
                    default="",
                    help="All letters that we know are not in the word, all in one string. Default is '' (emtpy string).")
parser.add_argument('-r', '--pattern',
                    default=".....",
                    help="Regex pattern we know the word must match. Default is '.....'.")
args = parser.parse_args()

# read the dictionary file, filter out those which are five characters long:
lines = []
with open(args.dictionary) as f:
    lines = f.read().splitlines()
words = [line for line in lines if len(line) == 5]

# set parameters
present = [char for char in args.present] # letters that we know are in the word
not_present = [char for char in args.not_present]  # letters we know are not in the word
pattern = re.compile(args.pattern)

# filter words with all() and not any()
candidates = [word for word in words if 
    all([letter in word for letter in present]) and 
    not any([letter in word for letter in not_present]) and
    pattern.match(word)
]

print(candidates)
