def main():
    print("--- Begin report of books/frankenstein.txt ---")

    file_path = "books/frankenstein.txt"
    text = read_file(file_path)
    number_of_words = get_number_of_words(text)
    print(f"{number_of_words} words found in document\n")

    letters = count_letters_occurrence(text)

    lettersList = []
    for key, value in letters.items():
        if key.isalpha():
            lettersList.append({"name": key, "num": value})

    lettersList.sort(reverse=True, key=sort_on)
    for letter in lettersList:
        print(f"The '{letter['name']}' character was found {letter['num']} times")

    print("--- End report ---")


def sort_on(dict):
    return dict["num"]


def read_file(file_path):
    with open(file_path) as f:
        return f.read()


def get_number_of_words(text):
    words = text.split()
    return len(words)


def count_letters_occurrence(text):
    letters = {}
    for letter in text:
        letterLower = letter.lower()
        if letterLower in letters:
            letters[letterLower] += 1
        else:
            letters[letterLower] = 1
    return letters


main()
