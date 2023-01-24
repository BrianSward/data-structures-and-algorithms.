def insert_sort(lst_):

    if lst_ is None:
        return None

    if not lst_:
        return []

    for i in range(1, len(lst_)):

        # this is where enumerate would come in handy
        cur_value = lst_[i]
        pos = i

        while pos > 0 and lst_[pos - 1] > cur_value:
            lst_[pos] = lst_[pos - 1]
            pos = pos - 1

        lst_[pos] = cur_value

    return lst_
