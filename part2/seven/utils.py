def find_pairs(number_list, total):
    result = []
    partials = {}

    for n in number_list:
        element = total - n
        if element in partials:
            result.append((n, element))
        partials[n] = n
    return result