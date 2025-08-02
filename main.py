from stats import get_num_words
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        get_num_words(filepath)
    except FileNotFoundError:
        print("Book not found - Check the path to the book")
    except Exception as e:
        print(e)


main()
