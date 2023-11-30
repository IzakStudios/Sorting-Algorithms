def bubble_sort(items):
    iteration_count = 0

    while True:
        has_swapped = False

        for i in range(len(items) - 1 - iteration_count):
            x = i
            y = i + 1

            if items[x] > items[y]:
                has_swapped = True
                items[x], items[y] = items[y], items[x]

        if not has_swapped:
            break

        iteration_count += 1
