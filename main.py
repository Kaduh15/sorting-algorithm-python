from collections import deque
import random
from timeit import timeit

# from stack import Stack


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


def test_time(x: int = 1):
    """
    It prints a message, creates a list of numbers, and then times how long it
    takes to sort the list
    using the built-in Python function sorted() and my function sorte()

    :param x: int = 1, defaults to 1
    :type x: int (optional)
    """
    print(("=" * 10) + f" \033[32m Testing time {x}X\033[0m  " + ("=" * 10))
    numbers = range(1, 10_001)
    total_numbers = len(numbers)
    len_max_numbers = total_numbers if x * 5 > total_numbers else x * 5

    numbers = random.sample(numbers, len_max_numbers)
    total_items = len(numbers)

    numbers_1 = numbers.copy()
    numbers_2 = numbers.copy()

    print(
        (
            f"Foi ordenado uma list de {total_items} itens\n"
            f"Em \033[32m{timeit(lambda: sorte(numbers_1))}\033[0m segundos\n"
            f"\033[33m* usando a minha função -> sorte()\033[0m\n"
        )
    )

    print(
        (
            f"Foi ordenado uma list de {total_items} itens\n"
            f"Em \033[32m{timeit(lambda: sorted(numbers_2))}\033[0m segundos\n"
            f"\033[33m* com a função nativa do Python -> sorted()\033[0m\n"
        )
    )


if __name__ == "__main__":
    test_time(1)
    test_time(100)
