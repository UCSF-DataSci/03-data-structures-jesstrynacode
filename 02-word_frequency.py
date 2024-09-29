#!/usr/bin/env python3
"""
Word Frequency Counter

This script reads a text file and counts the frequency of each word, ignoring case.

Usage: python word_frequency.py <input_file>


Your task:
- Complete the word_frequency() function to count word frequencies sorted alphabetically
- Test your script on 'alice_in_wonderland.txt'

Hints:
- Use a dictionary to store word frequencies
- Consider using the lower() method to ignore case
- The split() method can be useful for splitting text into words
"""

import sys
import re

def word_frequency(text: str):
    text = text.lower() #ignore case
    text = re.sub(r'[^a-z0-9\s]', '', text) #remove everything except spaces and alphanumeric characters
    words = text.split() #split text into words by whitespace
    frequencies = {} # Dictionary to store word frequencies

    #function to count frequency of each word
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    sorted_list = sorted(frequencies.items()) #creating new sorted list in alphabetical order
    
    sorted_list_20 = sorted_list[:20]

    return sorted_list_20

# Scaffold for opening a file and running word_frequency() on the contents
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_frequency.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            text = file.read() # Read the entire file into a string
        
        frequencies = word_frequency(text)
        
        # Print results
        for word, count in frequencies.items():
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    
    print(f"Word frequencies for '{filename}':")
    print(frequencies)