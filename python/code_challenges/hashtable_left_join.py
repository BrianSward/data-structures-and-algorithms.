try:
    from python.data_structures.hashtable import Hashtable
except:
    from data_structures.hashtable import Hashtable

def left_join(h_table_a, h_table_b):
    if not h_table_a:
        return None
    return_me = []
    for thing in h_table_a:
        if not h_table_b.get(thing):
            save_me = [thing, h_table_a[thing], "NONE"]
        else:
            save_me = [thing, h_table_a[thing], h_table_b.get(thing)]
        return_me.append(save_me)
    return return_me
