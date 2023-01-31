def first_repeated_word(str):
    """
    this function will take in a string from the user and return to them a sting which contains
    the first word that repeats in the string. if none, returns None
    :param str:
    :return: a string which will be the first word repeated. if none, returns None
    """
    # remove punctuation
    punc_table = "~`!@#$%^&*()_-+={}|[]\:;'<,>.?/"
    punc_table_2 = '"'
    for let in str:
        if let in (punc_table or punc_table_2):
            str = str.replace(let, "")
    # break it up
    words = str.split()
    word_set = set()
    # check for doubles
    for word in words:
        if word.lower() in word_set:
            return word.lower()
        word_set.add(word.lower())
    return None
