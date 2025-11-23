import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    file_contents = ()
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    return get_book_text(sys.argv[1])

from stats import get_num_words

from stats import get_num_characters

num_char = get_num_characters(main())
#print(num_char)

from stats import sort_list

#sorted_list = sort_list(num_char)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
get_num_words(main())
print("--------- Character Count -------")
sort_list(num_char)