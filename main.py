def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        word_count = count_words(file_contents)
        sorted_dict = count_chars(file_contents)
        print("Word Count:", word_count)
        print(sorted_dict)
    
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



main()

