import time, random

to_sort = [random.randint(0, 10) for _ in range(10)]


def is_sorted(sorting_list, override):
    if not override:
        return

    for index, item in enumerate(sorting_list[1:]):
        if sorting_list[index] > item:
            return False
    return True

print(to_sort)

index = 0
sorting_list = to_sort
start = time.time()
override = False

while not is_sorted(sorting_list, override):
    override = False
    if sorting_list[index] > sorting_list[index+1]:
        to_insert = sorting_list[index+1]
        del sorting_list[index+1]
        for i, item in enumerate(sorting_list):
            if item > to_insert:
                sorting_list.insert(i, to_insert)
                break
    index += 1
    if index == len(sorting_list) - 1:
        index = 0
        override = True
    print(sorting_list)

print("Took: ", time.time() - start)
