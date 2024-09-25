def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    report = prepare_report(book_path, text)
    print_report(report)


def get_book_text(path: str) -> str:
    with open(path,"r") as file:
        return file.read()
    

def get_word_count(book: str) -> int:
    words = book.split()
    return len(words)


def format_text(text: list) -> str:
    formatted_text = "".join(text).lower()
    return formatted_text


def get_char_count(formatted_text: str) -> dict:
    char_counter = {}
    for char in formatted_text:
            if char.isalpha():
                if char not in char_counter.keys():
                    char_counter[char] = 1
                else:
                    char_counter[char] += 1 

    return char_counter

def prepare_report(book_path: str, text: str):
    title = book_path.split("/")[1].capitalize()
    word_count: int = get_word_count(text)
    char_count: dict = get_char_count(format_text(text))
    sorted_char_count: dict = dict(sorted(char_count.items(), key=lambda char_count:char_count[1], reverse=True))

    return title, word_count, sorted_char_count



def print_report(report):
    title, word_count, char_count = report
    print(f"--- Begin report for Title: {title} --- \n Word Count: {word_count}\n")
    for key in char_count.keys():
        print(f"The ('{key}') character was found {char_count[key]} times")
    print("--- END Report ---")

    



if __name__ == "__main__":
    main()

