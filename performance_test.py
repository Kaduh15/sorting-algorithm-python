import random
from timeit import timeit

from main import sorte


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
