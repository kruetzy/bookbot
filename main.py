def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
    
    word_count = count_words(file_contents)
    sorted_dict = count_chars(file_contents)
    
    isalpha_list = letter_count_list(sorted_dict)
    isalpha_list.sort(key=lambda x: x[1], reverse=True)

    # creating report
    def print_report():
        print("--- Begin report of books/frankenstein.txt --- \n")
        print(f"{word_count} words found in the document \n")
        for x in isalpha_list:
            print(f"The '{x[0]}' character was found {x[1]} times")
        print("\n --- End report ---")

    print_report()

def count_words(book):
    words = book.split()
    return len(words)
    

def count_chars(book):
    # convert all chars in string to lowercase
    book_lower = book.lower()
    # create empty dict for loop
    count_dict = {}
    # loop through each character in string
    for char in book_lower:
        # add character to dictionary if it's not in it
        if char not in count_dict:
            count_dict[char] = 1
        # if in dict, increase the count by one
        else:
            count_dict[char] += 1
    sorted_dict = dict(sorted(count_dict.items()))
    return sorted_dict

def letter_count_list(dict):
    isalpha_list = [(key, value) for key, value in dict.items() if key.isalpha()]
    #print(isalpha_list)
    return isalpha_list
    


main()

