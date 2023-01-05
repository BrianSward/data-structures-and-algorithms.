from queue import Queue


def multi_bracket_validation(my_str):
    """
    this function will take in a string, look for the symbols in the lists below
    and checks for pairs in the correct order
    """

    # target symbols
    opening_symbols = ["[", "{", "("]
    closing_symbols = ["]", "}", ")"]

    # space to put things
    my_targets = []

    # iterate through my str and look for symbols, upon encounter do logic
    for i in my_str:
        if i in opening_symbols:
            my_targets.append(i)
        elif i in closing_symbols:
            pointer = closing_symbols.index(i)
            if ((len(my_targets) > 0) and
                    (opening_symbols[pointer] == my_targets[len(my_targets) - 1])):
                my_targets.pop()
            else:
                return False
    if len(my_targets) > 0:
        return False
    else:
        return True


if __name__ == '__main__':
    print(multi_bracket_validation("()[[Extra Characters]]"))
