import sys
from stats import get_word_count as gwc
from stats import create_dict_of_char_counts as cdc
from stats import sort_dict_by_value as sdbv
from stats import produce_book_report as pbr

# function to open and read book files
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    """
    Main function to execute the book analysis. It reads the book file 
    specified in the command line argument,
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1] # Use the provided file path from command line argument
    book = get_book_text(file_path)
    num_words = gwc(book)
    char_dict = cdc(book)
    sorted_char_dict = sdbv(char_dict)
    report = pbr(num_words, sorted_char_dict, file_path)
    print(report)

if __name__ == "__main__":
    main()