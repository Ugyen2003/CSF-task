def is_sorted(lst):
    return all(lst[1] <= lst[i + 1] for i in range(len(lst) -1))