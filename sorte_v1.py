def sorte(list: list[int]) -> list[int]:
    """
    It sorts a list of integers by recursively finding the
    minimum and maximum values of the list,
    appending them to a new list, and then removing them from the original list
    :param list: list[int] -> The list of integers to be sorted
    :type list: list[int]
    :return: A list with the smallest and largest values of the list.
    """
    if len(list) == 0:
        return

    result = []

    min, max = menor_maior(list)
    result.append(min)
    result.append(max)
    list.remove(min)
    if max in list:
        list.remove(max)

    sorted_list = sorte(list)

    if not sorted_list:
        return result

    sorted_list.append(result[-1])
    sorted_list.insert(0, result[0])

    return sorted_list


def menor_maior(list: list[int]):
    """
    It returns the minimum and maximum values in a list
    :param list: list[int]: This is the list of integers
                            that we're going to be searching through
    :type list: list[int]
    :return: A tuple with the minimum and maximum values of the list.
    """
    min = list[0]
    max = min
    for value in list:
        if value < min:
            min = value
        if value > max:
            max = value
    return (min, max)
