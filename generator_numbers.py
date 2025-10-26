import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Аналізує текст, знаходить всі дійсні числа та повертає їх як генератор.

    Args:
        text (str): Вхідний рядок для аналізу.

    Yields:
        Generator[float, None, None]: Генератор, що повертає дійсні числа.
    """
    # Регулярний вираз для пошуку дійсних чисел, що відокремлені пробілами
    # \b - межа слова, щоб уникнути захоплення чисел, які є частиною інших слів
    pattern = r"\b\d+\.\d+\b"
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Підсумовує числа, отримані від генератора.

    Args:
        text (str): Вхідний рядок для аналізу.
        func (Callable): Функція-генератор, яка буде викликана для отримання чисел.

    Returns:
        float: Загальна сума чисел.
    """
    return sum(func(text))


# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, \
    доповнений додатковими надходженнями 27.45 та 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

