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

    # print(letter_dictionary)
            
    print("------------------ Begin Report ----------------")
    print(f"There were {len(words)} in the document.")

    # Creating a report
    # Convert the dictionary to a list so that we can sort.
    # letter_list = list(letter_dictionary)
    # print(letter_list, type(letter_list))
    # print(letter_list.sort())

    letter_list = []

    # for key in letter_dictionary:
        
    #     if key.isalpha():
    #         letter_list.append(key)
    #         print(f"The character '{key}' was found {letter_dictionary[key]} times in the text.")

    # print(f"The list of letter in alphabetical order:\\n{sorted(letter_list)}")

    for key in letter_dictionary:
    
        if key.isalpha():
            letter_list.append({"char": key,"number": letter_dictionary[key]})
            # print(f"The character '{key}' was found {letter_dictionary[key]} times in the text.")

    # print(letter_list)
    # letter_list.sort(reverse=True)
    # print(f"Sorted list: {letter_list}")
    
    for dict in letter_list:
        print(f"The character '{dict["char"]} was found {dict["number"]} times in the text.")
print("------------------ End Report ----------------")
    # print(f"The list of letter in alphabetical order:\\n{sorted(letter_list)}")

# Here is Book.dev's solution
# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)``
#     print(f"{num_words} words found in the document")


# def get_num_words(text):
#     words = text.split()
#     return len(words)


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()


# main()