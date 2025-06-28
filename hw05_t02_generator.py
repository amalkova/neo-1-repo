#Завдання 2 - generator_numbers

import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генерує всі дійсні числа з тексту як числа з плаваючою крапкою.
    Числа у тексті мають бути відокремлені пробілами.
    """
    # Пошук усіх дійсних чисел з крапкою у тексті
    numbers = re.findall(r'\b\d+\.\d+\b', text)
    for number in numbers:
        yield float(number)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює загальну суму чисел з тексту, використовуючи передану функцію-генератор.
    """
    return sum(func(text))