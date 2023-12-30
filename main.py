with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)

    words = file_contents.split()
    print(f"\n\nThe number of words in the book Frankenstein is {len(words)}")

    file_content_lowercase = file_contents.lower()
    
    # strip white space
    file_content_lowercase.strip()

    letter_dictionary = {}

    for letter in file_content_lowercase:
        # if not letter_dictionary[letter]:
        #     letter_dictionary[letter] = 1
        #     print (letter_dictionary)
        # else:
        #     letter_dictionary[letter] += 1

        if letter in letter_dictionary:
            letter_dictionary[letter] += 1
        else:
            letter_dictionary[letter] = 1

    print(letter_dictionary)


# Here is Book.dev's solution
# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     print(f"{num_words} words found in the document")


# def get_num_words(text):
#     words = text.split()
#     return len(words)


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()


# main()