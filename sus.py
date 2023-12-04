import ipaddress
import random

def ip_to_unique_words(ip_address, words_filename):
    # Read the list of words from the text file
    with open(words_filename, 'r') as f:
        words = f.read().splitlines()

    # Convert the IP address to an integer
    ip_int = int(ipaddress.ip_address(ip_address))

    # Convert the integer to a binary string
    binary_string = bin(ip_int)[2:]

    # Pad the binary string with zeros to make it a multiple of 8
    padded_binary_string = binary_string.zfill(8 * len(ip_address.split('.')))

    # Split the binary string into groups of 8 bits
    eight_bit_groups = [padded_binary_string[i:i+8] for i in range(0, len(padded_binary_string), 8)]

    # Convert each group of 8 bits to a decimal number
    decimal_numbers = [int(group, 2) for group in eight_bit_groups]

    # Convert each decimal number to a word using the dictionary
    unique_words = []
    for number in decimal_numbers:
        unique_words.append(words[number])

    # Shuffle the list of unique words
    random.shuffle(unique_words)

    # Return the list of unique words as a string
    return ' '.join(unique_words)

if __name__ == "__main__":
    ip_address = "84.3.29.42"
    words_filename = "words.txt"
    unique_words = ip_to_unique_words(ip_address, words_filename)
    print(unique_words)
