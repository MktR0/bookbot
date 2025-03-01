def get_word_count(book: str) -> int:
    words = book.split()
    return len(words)

def get_char_count(formatted_text: str) -> dict:
    char_counter = {}
    for char in formatted_text:
            if char.isalpha():
                if char not in char_counter.keys():
                    char_counter[char] = 1
                else:
                    char_counter[char] += 1 

    return char_counter

def sort_on(n):
    return n["num"]

def chars_dict_to_sorted_list(char_count):
    sorted_char_count: dict = dict(sorted(char_count.items(), key=lambda char_count:char_count[1], reverse=True))
    return sorted_char_count
