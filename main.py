def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_word = get_num_words(text)
    num_char = get_num_char(text)

    sorted_char_counts = chars_dict_to_sorted_list(num_char)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_word} words found in the document")
    print("\n")
    
    for item in sorted_char_counts:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
        else: 
            pass
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_char(text):
    dict = {}
    for c in text:
        lowered = c.lower()
        if lowered not in dict:
            dict[lowered] = 1
        else: 
            dict[lowered] += 1
    return dict 

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
