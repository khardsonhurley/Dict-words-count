# put your code here.

def word_count(file_name):
    test_file = open(file_name)

    words_list = []
    words_dict = {}

    for line in test_file:
        line_list = line.rstrip().split(" ")
        words_list = words_list + line_list

    test_file.close()

    for word in words_list:
        words_dict[word] = words_dict.get(word,0) + 1

    for words, count in words_dict.iteritems():
        print words, count

word_count("test.txt")