import sys

from stats import (
        get_word_count,
        get_char_count,
        chars_dict_to_sorted_list,
        )
def main():
    try:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        report = prepare_report(book_path, text)
        final_report = generate_report(report, book_path)
        print_report(final_report, book_path)
    except Exception:
        print("Usage: py(thon3) main.py <path_to_book>")
        sys.exit(1)


def get_book_text(path: str) -> str:
    with open(path,"r") as file:
        return file.read()

def format_input_text(text: list) -> str:
    formatted_text = "".join(text).lower()
    return formatted_text


def prepare_report(book_path: str, text: str):
    title = book_path.split("/")[1].capitalize()
    word_count: int = get_word_count(text)
    chars  = text.split()
    char_count: dict = get_char_count(format_input_text(chars))
    sorted_char_count = chars_dict_to_sorted_list(char_count)
    return title, word_count, sorted_char_count

def generate_report(report, book_path):
    final_report = []
    title, word_count, char_count = report
    final_report.append("============ BOOKBOT ============")
    final_report.append(f"Analyzing book {title} found at {book_path}...")
    final_report.append("----------- Word Count ----------")
    final_report.append(f"Found {word_count} total words")
    final_report.append("--------- Character Count -------")
    for key in char_count.keys():
        final_report.append(f"{key}: {char_count[key]}")

    final_report.append("============= END ===============")

    return final_report


def print_report(final_report, book_path):

    def format_output_text(line,length, format_type):
        right_align = length - len(line)
        left_align = len(line) - length
        center_align = (length - len(line)) // 2

        if format_type == "right":
            return " " * right_align + line

        if format_type == "left":
            return " " * left_align + line

        if format_type == "center":
            return " "* center_align + line

    title = final_report[1]
    length = len(f"Analyzing book {title} found at {book_path}...") // 2
    for i in range(len(final_report)):
        if final_report[i]  == title:
            print(title)
            continue
        line = format_output_text(final_report[i],length=length,format_type="center")
        print(line)


if __name__ == "__main__":
    main()

