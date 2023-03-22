from collections import deque


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
    if len(list) == 1:
        deque().append(list[0])

    result = deque()
    min_value = min(list)

    result.append(min_value)
    list.remove(min_value)
    if len(list) > 0:
        max_value = max(list)
        result.append(max_value)
        list.remove(max_value)

    sorted_list = sorte(list)

    if not sorted_list:
        return result

    sorted_list.append(result.pop())
    sorted_list.appendleft(result.pop())

    return sorted_list
