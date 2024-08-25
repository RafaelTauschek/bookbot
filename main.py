def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_characters(text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words fround in the document")
    print("")
    
    
    for item in chars_dict_sorted(char_count):
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
            #print(f"The {item["char"]} character was found {item["num"]} times")
    
    print("--- End report ---")
    


def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_dict = {}
    for c in text:
        lowerd = c.lower()
        if lowerd in char_dict:
            char_dict[lowerd] += 1
        else:
            char_dict[lowerd] = 1
            
    return char_dict


def sort_on(d):
    return d["num"]
    
def chars_dict_sorted(char_dict):
    result = []
    
    for c in char_dict:
        result.append({"char": c, "num": char_dict[c]})
    result.sort(reverse=True, key=sort_on)
    
    return result

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

    


main()