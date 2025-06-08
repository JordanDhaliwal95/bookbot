from stats import get_num_words, get_chars_dict, sorted_chars_dict
import sys
print(sys.argv)
if sys.argv and len(sys.argv) == 2:
    book_path = sys.argv[1]
    
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"Found {num_words} total words")
    print(sorted_chars_dict(chars_dict))
    sys.exit(0)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
