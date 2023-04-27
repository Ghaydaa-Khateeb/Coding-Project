import random
import math
from collections import defaultdict
import numpy as np
def generate_random_sequence(symbols, probabilities, length):
    """
    Generates a random sequence of symbols with given probabilities and length.
    """
    return random.choices(symbols, probabilities, k=length)

def calculate_entropy(symbols, probabilities):
    """Calculate the source entropy in bits"""
    H = 0
    for symbol, probability in zip(symbols, probabilities):
        H -= probability * math.log2(probability)
    return H

def parse_and_assign_numbers(sequence):
    """
    Parses a sequence of symbols and assigns a number to each phrase using LZ78 algorithm.
    """
    dictionary = {'': 0}
    phrase = ''
    last_phrase = ''
    str1 = ''
    encoded_sequence = []
    for symbol in sequence:
        phrase += symbol
        str1 += symbol
        if phrase not in dictionary:
            x = calculate_number_of_appearance(dictionary,phrase)
            dictionary[phrase] = x
            encoded_sequence.append((dictionary[last_phrase], symbol))
            last_phrase = phrase
            phrase = ""

        else:
            last_phrase = phrase
    dictionary.pop('',0)
    return dictionary

def calculate_number_of_appearance(dictioenary , symbol):
    x=0
    for i in dictioenary:
        a = symbol[:-1]
        if(i==a):
            return x
        x+=1
    return 0

def calculate_nb(encoded_sequence):
    """
    Calculates the number of binary digits needed to encode a given sequence.
    """
    nb = (((math.ceil(math.log2(len(encoded_sequence))))+8)*len(encoded_sequence))
    return nb

def calculate_average_nb(symbols, probabilities, length, iterations):
    """
    Generates random sequences, encodes them using LZ78 algorithm, and calculates the average number of binary digits.
    """
    average_nb = 0
    for i in range(iterations):
        sequence = generate_random_sequence(symbols, probabilities, length)
        encoded_sequence = parse_and_assign_numbers(sequence)
        nb = calculate_nb(encoded_sequence)
        average_nb += nb
    return average_nb / iterations

def calculate_compression_ratio(average_nb, length):
    """
    Calculates the compression ratio relative to the ASCII code.
    """
    return average_nb / (length * 8)

    # Main program
symbols = ['a', 'b', 'c', 'd']
probabilities = [0.4, 0.3, 0.2, 0.1]
length = 20
iterations = 5

sequence = generate_random_sequence(symbols, probabilities, length)
print("Sequence:", ''.join(sequence))

# Calculate the source entropy
H = calculate_entropy(symbols, probabilities)
print("Entropy :",H, "bits/symbols")

encoded_sequence = parse_and_assign_numbers(sequence)
enq = {'': 0}
p = []
   # for index in range(len(encoded_sequence)):
        #print(encoded_sequence.items())
        #print(p)

print("**************************************************")
print("Dictionary content: ", encoded_sequence.keys())
print("Encoded Packets:", encoded_sequence)
print("**************************************************\n")

import pandas as pd
print("Sequence length".ljust(20) + "|" + "Number of binary digits (NB)".ljust(45) + "|" + "Number of bits per symbol".ljust(30)
      + "|" + "Compression ratio")
print("-"*120)
sequence_lengths = [20, 50, 100, 200, 400, 800, 1000, 2000]
for length in sequence_lengths:
    sequence = generate_random_sequence(symbols, probabilities, length)
    encoded_sequence = parse_and_assign_numbers(sequence)
    nb = calculate_nb(encoded_sequence)
    average_nb = calculate_average_nb(symbols, probabilities, length, iterations)
    compression_ratio = calculate_compression_ratio(average_nb, length)

    print(str(length).ljust(20) + "|" + str(nb).ljust(45) + "|" + str(nb / length).ljust(30) + "|" + str(compression_ratio*100))
