import time, random

unsorted = [random.randint(0, 999) for _ in range(999)]

search = unsorted[random.randint(0, len(unsorted)-1)]

start = time.time()
for item in unsorted:
    if item == search:
        break

print("Took: ", time.time() - start)
