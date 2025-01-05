def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    word_count = get_words_count(text)
    print(text)
    print(f"total word count: {word_count}")
    print(get_character_count(text))

def get_character_count(dict):
    path_to_file = "books/frankenstein.txt"
    character_count = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    for string in get_book_text(path_to_file.lower()):
        for character in string:
            if character in character_count:
                character_count[character] += 1
    return character_count

def get_words_count(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()