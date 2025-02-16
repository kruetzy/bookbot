def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        count_words(file_contents)
        count_chars(file_contents)
    
def count_words(book):
    words = book.split()
    print(len(words))
    

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
    print(sorted_dict)



main()

