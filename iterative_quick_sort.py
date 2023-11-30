def partition(items, start, end):
    pivot = items[end]

    pointer_0 = start
    pointer_1 = start

    while pointer_1 <= end:
        if (items[pointer_1] < pivot):
            items[pointer_0], items[pointer_1] = items[pointer_1], items[pointer_0]
            pointer_0 += 1
        
        pointer_1 += 1

    items[pointer_0], items[end] = items[end], items[pointer_0]

    return pointer_0

def iterative_quick_sort(items):
    if not items: return
    if len(items) <= 1: return

    start = 0
    end = len(items) - 1

    stack = []

    stack.append(start)
    stack.append(end)

    while len(stack) != 0:
        end = stack.pop()
        start = stack.pop()

        if start < end:
            pivot = partition(items, start, end)

            stack.append(start)
            stack.append(pivot - 1)

            stack.append(pivot + 1)
            stack.append(end)
