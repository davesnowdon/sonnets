import itertools
from collections import defaultdict
import random

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
    return len(' '.join(phrase)) / 6 + len(phrase)


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


for _ in range(14):
    phrase = get_shakesperian_phrase()
    print ' '.join([phrase[0].capitalize()] + phrase[1:])
