from collections import deque

from stack import Stack


def sorte(list: list[int]) -> list[int]:
    """
    It sorts a list of integers by recursively finding the
    minimum and maximum values of the list,
    appending them to a new list, and then removing them from the original list
    :param list: list[int] -> The list of integers to be sorted
    :type list: list[int]
    :return: A list with the smallest and largest values of the list.
    """
    list = list.copy()
    stack = Stack()
    result = deque()

    while len(list) > 0:
        menor_maior = []
        min_value = min(list)
        menor_maior.append(min_value)
        list.remove(min_value)
        if len(list) > 0:
            max_value = max(list)
            menor_maior.append(max_value)
            list.remove(max_value)
        stack.add(menor_maior)

    while len(stack) > 0:
        current_stack = stack.pop()
        if len(current_stack) == 1:
            result.append(current_stack[0])
        else:
            result.appendleft(current_stack[0])
            result.append(current_stack[1])

    return result
