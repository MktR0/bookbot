import sys

from stats import (
        get_word_count,
        get_char_count,
        )
def main():
    try:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        report = prepare_report(book_path, text)
        print_report(report, book_path)
    except Exception:
        print("Usage: py(thon3) main.py <path_to_book>")
        sys.exit(1)


def get_book_text(path: str) -> str:
    with open(path,"r") as file:
        return file.read()

def format_text(text: list) -> str:
    formatted_text = "".join(text).lower()
    return formatted_text


def prepare_report(book_path: str, text: str):
    title = book_path.split("/")[1].capitalize()
    word_count: int = get_word_count(text)
    chars  = text.split()
    char_count: dict = get_char_count(format_text(chars))
    sorted_char_count: dict = dict(sorted(char_count.items(), key=lambda char_count:char_count[1], reverse=True))

    return title, word_count, sorted_char_count


report_data = []
def print_report(report, book_path):
    title, word_count, char_count = report
    print("============ BOOKBOT ============")
    print(f"Analyzing book {title} found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for key in char_count.keys():
        print(f"{key}: {char_count[key]}")

    print("============= END ===============")


if __name__ == "__main__":
    main()

