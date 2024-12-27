# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def char_count(text):
    text = text.lower()

    char_dict = dict()

    for char in text:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 0
    
    return char_dict

def count_words(text):
    return len(text.split())

def get_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path)
    book_num_words = count_words(book_text)
    num_of_char = char_count(book_text)

    list_num_of_char = [{"char": key, "num": value} for key, value in num_of_char.items()]
    list_num_of_char.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{book_num_words} words found in the document")
    print()

    for char_set in list_num_of_char:
        print(f"The '{char_set['char']}' character was found {char_set['num']} times")
    
    print("--- End report ---")

main()