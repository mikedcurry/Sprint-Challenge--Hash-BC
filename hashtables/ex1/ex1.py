#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    # Instantiate Hashtable
    ht = HashTable(16)

    # insert stuff into hashtable
    for i in range(length):
        # WTH? I'm going to yield keys...
        hash_table_insert(ht, weights[i], i)

    for k in range(length):
        # weight[k] + weight2 = limit

        # Gives me the index of each of the other weight combined with to == limit
        index = hash_table_retrieve(ht, (limit - weights[k]))
        # Now I have to order the silly indices...
        if index:
            if index > i:
                return [index, i]
            else:
                return [i, index]

    # What if there is more than one solution? THis only gives one...
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
