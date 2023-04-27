import heapq
from collections import defaultdict
import math
from docx import Document

def build_tree(frequencies):
    heap = [[weight, [char, ""]] for char, weight in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap[0]

def huffman_code(text):
    frequencies = defaultdict(int)
    for char in text:
        frequencies[char] += 1
    tree = build_tree(frequencies)
    codes = {}
    for pair in tree[1:]:
        codes[pair[0]] = pair[1]
    return codes

def compress(text, codes):
    compressed_text = ""
    for char in text:
        compressed_text += codes[char]
    return compressed_text


def calculate_entropy(text):
    frequencies = defaultdict(int)
    for char in text:
        frequencies[char] += 1
    entropy = 0
    for char in frequencies:
        p = frequencies[char]/len(text)
        entropy += -p * math.log2(p)
    return entropy

def calculate_compression_ratio(text, compressed_text):
    return len(compressed_text) / (8 * len(text))

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
    compressed_text = compress(text, codes)
    average_bits_per_char = sum([len(codes[c])*round(frequencies[c],5) for c in frequencies])
    ascii_bits = 8 * len(text)
    compression_ratio = calculate_compression_ratio(text, compressed_text)
    entropy = 0
    for char in frequencies:
        p = round(frequencies[char],5)
        entropy += -p * math.log2(p)
        total = sum(frequencies.values())
    print("Probabilities: ", {s: f / total for s, f in frequencies.items()})
    huffman_codes = huffman_code(text)
    print("Codewords: ", codes)
    print("Length of codewords: ", {s: len(huffman_codes[s]) for s in frequencies.keys()})
    print("****************************************************************************")

    print("Average number of bits per character: ", average_bits_per_char)
    print("Number of bits needed using ASCII: ", ascii_bits)
    print("Compression ratio: ", compression_ratio)
    print("Entropy: ", entropy)

    print("****************************************************************************")
    # specific characters you want to print codeword for
    specific_chars = ['a', 'b', 'c','d','e','f','g','h',' ','.']
    huffman_codes = huffman_code(text)
    print("Character".ljust(10) + "|" + "Probability".ljust(25) + "|" + "Length of codeword".ljust(20) + "|" + "Codeword")
    print("-"*60)
    for char in specific_chars:
        if char in huffman_codes:
            print(char.ljust(10) + "|" + str(frequencies[char] / total).ljust(25) + "|" + str(len(huffman_codes[char])).ljust(20)
                  + "|" + huffman_codes[char])

        else:
            print(f"{char:<10} | Not found | Not found | Not found")

    f.close()

if __name__ == "__main__":
    main()
