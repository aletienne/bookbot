# This program reads a text file and prints its content to the console.

file_name = "frankenstein.txt"
def get_book_text(file_name):
      with open(file_name) as f:
        file = f.read()
        print(file)

get_book_text("books/" + file_name)