import heapq # importing the heapq library for building the Huffman tree
from collections import defaultdict # importing the defaultdict library for counting the frequency of characters in the text
import math # importing the math library for calculating the entropy

def build_tree(frequencies):
    """
    This function takes in the frequency of each character in the text and builds the Huffman tree.
    """
    # creating a list of lists where each inner list has the weight (frequency) and the character and an empty string as the codeword
    heap = [[weight, [char, ""]] for char, weight in frequencies.items()]
    heapq.heapify(heap) # converting the list to a heap
    # while the heap has more than one element, pop the two smallest elements (low and high)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        # for each element in the low heap, add a 0 as the prefix of the codeword
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        # for each element in the high heap, add a 1 as the prefix of the codeword
        for pair in hi[1:]:
            pair= '1' + pair[1]
# push the concatenation of low and high back to the heap
    heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap[0]

def huffman_code(text):
"""
This function takes in the text and generates the Huffman code of each character.
"""
frequencies = defaultdict(int) # creating a defaultdict to store the frequency of each character
for char in text:
    frequencies[char] += 1 # counting the frequency of each character
    tree = build_tree(frequencies) # building the Huffman tree
    codes = {} # creating an empty dictionary to store the Huffman code of each character
for pair in tree[1:]:
    codes[pair[0]] = pair[1] # storing the Huffman code of each character
return codes

def compress(text, codes):
"""
This function takes in the text and the Huffman codes and compresses the text using the Huffman codes.
"""
compressed_text = "" # creating an empty string to store the compressed text
for char in text:
 compressed_text += codes[char] # concatenating the Huffman code of each character to the compressed text
return compressed_text

def calculate_entropy(text):
"""
This function takes in the text and calculates the entropy of the text.
"""
frequencies = defaultdict(int) # creating a defaultdict to store the frequency of each character
for char in text:
    frequencies[char] += 1 # counting the frequency of each character
    entropy = 0 # initializing the entropy
for char in frequencies:
    p = frequencies[char]/len(text) # calculating the probability of each character
entropy += -p * math.log2(p) # calculating the entropy using the formula
return entropy

def calculate_compression_ratio(text, compressed_text):
"""
This function takes in the original text and the compressed text and calculates the compression ratio.
"""
return len(compressed_text) / (8 * len(text)) # dividing the length of the compressed text by the length of the original text (in bytes)

def main():
with open("TheBoardingHouse.txt", "r", encoding="utf-8") as f:
text = f.read()
text = ''.join(filter(lambda x: x.isprintable(), text))
text = text.lower() # ignore capitalization
text = text.replace("\n", "") # ignore newlines
frequencies = defaultdict(int)
for char in text:
frequencies[char] += 1
for char in frequencies:
frequencies[char] /= len(text)
frequencies[char] = round(frequencies[char], 5)
codes = huffman_code(text)
compressed_
