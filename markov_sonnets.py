import itertools
from collections import defaultdict
import random
import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
from string import punctuation

pron_dict = cmudict.dict()

f = open('pg1041.txt')

lines = f.readlines()
lines = [line for line in lines if len(line) > 20]
lines = [line.replace('.', '') for line in lines]
lines = [line.replace(',', '') for line in lines]
lines = [line.replace('"', '') for line in lines]
lines = [line.replace(':', '') for line in lines]
lines = [line.replace(';', '') for line in lines]
lines = [line.strip() for line in lines]
lines = [[word.lower() for word in line.split()] for line in lines]
words = list(itertools.chain(*lines))

pairs = defaultdict(list)

for word1, word2 in [words[i:i+2] for i in range(len(words) - 1)]:
    pairs[word1].append(word2)


def get_num_syllables(phrase):
    num_syllables = [nsyl(w.strip(punctuation)) for w in phrase]
    return sum(num_syllables)

def nsyl(word):
    global pron_dict
    return max([len(list(y for y in x if isdigit(y[-1]))) for x in pron_dict[word.lower()]])

def try_get_shakesperian_phrase():
    phrase = [random.choice(pairs.keys())]
    while True:
        phrase.append(random.choice(pairs[phrase[-1]]))
        num_syllables = get_num_syllables(phrase)
        if num_syllables == 10:
            return phrase
        elif num_syllables > 10:
            raise Exception


def get_shakesperian_phrase():
    while True:
        try:
            return try_get_shakesperian_phrase()
        except:
            continue

if __name__ == "__main__":
    for _ in range(14):
        phrase = get_shakesperian_phrase()
        print ' '.join([phrase[0].capitalize()] + phrase[1:])
