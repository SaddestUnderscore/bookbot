def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    word_count = get_words_count(text)
    chars_list = list(get_character_count(text).items())

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")
    sorted_chars_list = sorted(chars_list, key=lambda item: item[1], reverse=True)
    for char, count in sorted_chars_list:
        print(f"The '{char}' character was found {count} times") 
    print("--- End report ---")

def get_character_count(text): # okay i need to print all the code i learned into my brain holy
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_words_count(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()