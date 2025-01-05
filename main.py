def main():
    word_count = 0
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        for string in file_contents.split():
            word_count += 1
    print(file_contents)
    print(f"total word count: {word_count}")

main()