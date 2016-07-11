# put your code here.

def punctuation_remove(my_string):
    """function to delete any punctuation

    more description here"""

    new_string = ""
    for letter in my_string:
        if letter == "," or letter == "?" or letter == ".":
            letter = ""
        new_string = new_string + letter
    return new_string

def word_count(file_name):
    """function to count occurences of words

    more description here"""

    test_file = open(file_name)

    words_list = []
    words_dict = {}

    for line in test_file:
        line_list = line.rstrip().split(" ")
        words_list = words_list + line_list
    print words_list

    test_file.close()

    for word in words_list:
        word = punctuation_remove(word).lower()
        words_dict[word] = words_dict.get(word,0) + 1
    print words_dict

    for words, count in words_dict.iteritems():
        print words, count

word_count("test.txt")
