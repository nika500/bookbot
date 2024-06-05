def main():
    with open("books/frankestein.txt") as f:
        text = f.read()
        print(text)
    print(get_number_of_words(text))
    print(count_letters_occurrence(text))

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