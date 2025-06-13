def count_words(book_string):
    word_list = book_string.split()
    return len(word_list)


def count_characters(book_string):
    book_string = book_string.lower()
    char_count = {}
    for i in range(0, len(book_string)):
        if book_string[i] not in char_count:
            char_count[book_string[i]] = 1
        else:
            char_count[book_string[i]] += 1
    return char_count