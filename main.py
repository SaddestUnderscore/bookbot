def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    word_count = get_words_count(text)
    print(text)
    print(f"total word count: {word_count}")
    print(get_character_count(text))

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