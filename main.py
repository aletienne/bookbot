# This program reads a text file and prints its content to the console.
from stats import get_num_words, get_num_char, sorted_list
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_name = sys.argv[1]

def get_book_text(file_name):
      with open(file_name) as f:
        file = f.read()
        return file

book = get_book_text(file_name)
words = get_num_words(book)
chars = get_num_char(book)
sorted= sorted_list(chars)

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print("Found " + words + " total words")
print("--------- Character Count -------")

for item in sorted:
    if item["char"].isalpha():
        print(item["char"] + ": " + str(item["num"]))