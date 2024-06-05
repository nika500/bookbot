def main():
    with open("books/frankestein.txt") as f:
        text = f.read()
        print(text)
    print(get_number_of_words(text))

def get_number_of_words(text):
    words = text.split()
    return len(words)

main()