def get_num_words(file):
    num_words = len(file.split())
    print(f"Found {num_words} total words")

def get_num_characters(file):
    num_char = {}
    for i in file.lower():
        if i not in num_char:
            num_char[i] = 1
        else:
            num_char[i] += 1
    return num_char

def sort_list(dict):
    sorted_list = []
    for key, value in dict.items():
        if key.isalpha():
            sorted_list.append({'char': key, 'num': value})
    sorted_list.sort(reverse=True, key=lambda list: list['num'])
    #print(sorted_list)
    for pair in sorted_list:
        print(f"{pair['char']}: {pair['num']}")