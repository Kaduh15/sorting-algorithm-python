from timeit import timeit


def sorte(list: list[int]) -> list[int]:
    if len(list) == 0:
        return

    result = []

    min = menor_maior(list)[0]
    max = menor_maior(list)[1]
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


def test_time(x: int = 1):
    """
    It prints a message, creates a list of numbers, and then times how long it
    takes to sort the list
    using the built-in Python function sorted() and my function sorte()

    :param x: int = 1, defaults to 1
    :type x: int (optional)
    """
    print(('=' * 10) + f" \033[32m Testing time {x}X\033[0m  " + ('=' * 10))
    numbers = [1, 2, 3, 4, 5]
    numbers = numbers * x
    total_items = len(numbers)
    print(
        f'''Foi ordenado uma list de {total_items} itens\b
Em \033[32m{timeit(lambda: sorted(numbers))}\033[0m segundos
\033[33m* com a função nativa do Python -> sorted()\033[0m''')

    print(
        f'''
Foi ordenado uma list de {total_items} itens
Em \033[32m{timeit(lambda: sorte(numbers))}\033[0m segundos
\033[33m* usando a minha função -> sorte()
\033[0m''')


if __name__ == '__main__':
    test_time(1)
    test_time(100)
