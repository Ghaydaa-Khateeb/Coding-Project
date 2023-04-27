import random
from collections import defaultdict

# Generate a random sequence of symbols
import np as np

symbols = ['a', 'b', 'c', 'd']
probabilities = [0.4, 0.3, 0.2, 0.1]
sequence = random.choices(symbols, probabilities, k=20)
print("Sequence:", ''.join(sequence))

# Calculate the source entropy
prob_dict = defaultdict(float)
for symbol in sequence:
    prob_dict[symbol] += 1/20
entropy = sum(-p * (np.log2(p)) for p in prob_dict.values())
print("Source entropy:", entropy, "bits")

# Parse the data and assign a number to each phrase
dictionary = {}
phrase = ""
phrase_num = 1
encoded_sequence = []
for symbol in sequence:
    phrase += symbol
    if phrase not in dictionary:
        dictionary[phrase] = phrase_num
        encoded_sequence.append((0, symbol))
        phrase = ""
        phrase_num += 1
    else:
        encoded_sequence.append((dictionary[phrase[:-1]], symbol))

print("Encoded sequence:", encoded_sequence)

# Find the number of binary digits needed to encode the sequence
# and the number of bits per symbol
nb = 0
for phrase_num, symbol in encoded_sequence:
    nb += len(bin(phrase_num)[2:]) + 8
print("Number of binary digits (NB):", nb)
print("Number of bits per symbol:", nb/20)

# Repeat parts 4 and 5 five times and find the average value of (NB)
average_nb = 0
for i in range(5):
    # Generate a new random sequence
    sequence = random.choices(symbols, probabilities, k=20)

    # Parse the data and assign a number to each phrase
    dictionary = {}
    phrase = ""
    phrase_num = 1
    encoded_sequence = []
    for symbol in sequence:
        phrase += symbol
        if phrase not in dictionary:
            dictionary[phrase] = phrase_num
            encoded_sequence.append((0, symbol))
            phrase = ""
            phrase_num += 1
        else:
            encoded_sequence.append((dictionary[phrase[:-1]], symbol))

    # Find the number of binary digits needed to encode the sequence
    nb = 0
    for phrase_num, symbol in encoded_sequence:
        nb += len(bin(phrase_num)[2:]) + 8
    average_nb += nb

average_nb /= 5
print("Average number of binary digits (NB):", average_nb)

# Find the compression ratio relative to the ASCII code
compression_ratio = average_nb / (20*8)
print("Compression ratio:", compression_ratio)
