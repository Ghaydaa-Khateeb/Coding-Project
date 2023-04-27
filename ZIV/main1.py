import random
import math

def generate_sequence(symbols, probabilities, length):
    """Generates a random sequence of symbols with given probabilities"""
    return random.choices(symbols, probabilities, k=length)

def calculate_entropy(symbols, probabilities):
    """Calculates the source entropy in bits for given symbols and probabilities"""
    entropy = 0
    for symbol, probability in zip(symbols, probabilities):
        entropy -= probability * math.log2(probability)
    return entropy

def assign_numbers(symbols):
    """Assigns a number to each phrase"""
    phrase_to_num = {}
    for i, symbol in enumerate(symbols):
        phrase_to_num[symbol] = i
    return phrase_to_num

def calculate_n_bits(entropy, length):
    """Calculates the number of binary digits needed to encode a sequence"""
    return entropy * length

def calculate_bits_per_symbol(n_bits, length):
    """Calculates the number of bits per symbol"""
    return n_bits / length

def repeat_and_average(symbols, probabilities, length, n_iterations):
    """Repeats the above steps n_iterations times and finds the average value of n_bits"""
    total_n_bits = 0
    for i in range(n_iterations):
        sequence = generate_sequence(symbols, probabilities, length)
        entropy = calculate_entropy(symbols, probabilities)
        n_bits = calculate_n_bits(entropy, len(sequence))
        total_n_bits += n_bits
    avg_n_bits = total_n_bits / n_iterations
    return avg_n_bits

def calculate_compression_ratio(avg_n_bits, length):
    """Calculates the compression ratio relative to the ASCII code"""
    return avg_n_bits / (length * 8)

def compress_sequence(sequence):
    """Compress a given sequence using the Lempel-Ziv algorithm"""
    dictionary = {}
    dictionary_index = 0
    compressed = []
    current_pattern = sequence[0]
    for i in range(1, len(sequence)):
        if sequence[i] not in current_pattern:
            if current_pattern in dictionary:
                compressed.append(dictionary[current_pattern])
            else:
                dictionary[current_pattern] = dictionary_index
                dictionary_index += 1
                compressed.append(dictionary[current_pattern])
            current_pattern = sequence[i]
        else:
            current_pattern += sequence[i]
    compressed.append(dictionary[current_pattern])
    return compressed,dictionary

symbols = ['a', 'b', 'c', 'd']
probabilities = [0.4, 0.3, 0.2, 0.1]
sequence = generate_sequence(symbols, probabilities, 20)

entropy = calculate_entropy(symbols, probabilities)
print("Entropy (bits): ", entropy)

phrase_to_num = assign_numbers(symbols)
print("Phrase to Number: ", phrase_to_num)

compressed_sequence,dictionary = compress_sequence(sequence)
print("Original Sequence: ", sequence)
print("Compressed Sequence: ", compressed_sequence)
print("Dictionary: ", dictionary)

n_bits = calculate_n_bits(entropy, len(compressed_sequence))
print("Number of Bits: ", n_bits)

bits_per_symbol = calculate_bits_per_symbol(n_bits, len(compressed_sequence))
print("Bits per Symbol: ", bits_per_symbol)

avg_n_bits = repeat_and_average(symbols, probabilities, 20, 5)
print("Average Number of Bits: ", avg_n_bits)

compression_ratio = calculate_compression_ratio(avg_n_bits, 20)
print("Compression Ratio: ", compression_ratio)

