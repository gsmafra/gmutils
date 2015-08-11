def most_common(l):

    return max(set(l), key=l.count)


def unique_elements(l):

    return list(set(l))


def indexes_matching(l, item):

    return [i for i, x in enumerate(l) if x == item]


def sub_list(l, index):

    return [l[i] for i in list(index)]


def join_lists(l):

    return [item for sublist in l for item in sublist]


def replicate_list(l, n):

    return join_lists([[item]*n for item in l])
