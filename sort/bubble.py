import time, random

to_sort = [random.randint(0, 1000) for _ in range(1000)]


def is_sorted(sorting_list, override):
    if not override:
        return

    for index, item in enumerate(sorting_list[1:]):
        if sorting_list[index] > item:
            return False
    return True


bubble = 0
sorting_list = to_sort
start = time.time()
override = False
while not is_sorted(sorting_list, override):
    override = False
    try:
        if sorting_list[bubble] > sorting_list[bubble+1]:
            sorting_list[bubble], sorting_list[bubble+1] = sorting_list[bubble+1], sorting_list[bubble]
    except IndexError:
        bubble = 0
        override = True
    else:
        bubble += 1

print(sorting_list)
print("Took: ", time.time() - start)
