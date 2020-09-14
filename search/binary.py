import time, random

search_list = [n for n in range(100)]
search = search_list[random.randint(0, len(search_list)-1)]

print("Search: ", search)


def split_and_search(to_search):
    """
    Recursive function to split given list in half,
    if middle value isnt search item,
    takes the correct half and calls itself again
    :param to_search: list to split and search
    """
    index = int(len(to_search)/2)
    middle_val = to_search[index]

    print(to_search, middle_val)

    if middle_val == search:
        return
    elif middle_val > search:
        split_and_search(to_search[:index])
    else:
        split_and_search(to_search[index:])


start = time.time()
split_and_search(search_list)
print("Took: ", time.time() - start)
