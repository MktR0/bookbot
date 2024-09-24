def main():
    book_path = "books/frankenstein.txt"
    title = book_path.split("/")[1].capitalize()
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(f"Title: {title} \nWord Count: {word_count}")


def get_book_text(path):
    with open(path,"r") as file:
        return file.read()
    

def get_word_count(book):
    words = book.split()
    return len(words)



main()
