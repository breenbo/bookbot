def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def get_char_count(text: str):
    char_dict: dict[str, int] = {}
    words = text.split()
    for word in words:
        for char in word:
            if char.isalpha():
                lower_char = char.lower()
                if lower_char in char_dict:
                    char_dict[lower_char] += 1
                else:
                    char_dict[lower_char] = 1

    return char_dict


def sort_on(items):
    return items["num"]


def sort_char_dict(char_dict: dict[str, int]):
    char_list= []
    for char in char_dict:
        char_list.append({"char": char, "num": char_dict[char]})

    char_list.sort(reverse=True, key=sort_on)

    return char_list


def pretty_print(filepath: str, word_count: int, char_dict: dict[str, int]):
    sorted = sort_char_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char in sorted:
        print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============") 


def get_num_words(filepath: str):
    text = get_book_text(filepath)
    word_count = len(text.split())
    char_count = get_char_count(text)

    pretty_print(filepath, word_count, char_count)
