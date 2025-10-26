from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    # Створюємо порожній словник для кешування
    cache: dict[int, int] = {}

    def fibonacci(n: int) -> int:
        # Перевіряємо базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1
        # Перевіряємо, чи є значення в кеші
        if n in cache:
            return cache[n]

        # Якщо значення немає в кеші, обчислюємо його рекурсивно,
        # зберігаємо у кеш та повертаємо результат
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаємо внутрішню функцію
    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію для обчислення чисел Фібоначчі
print(f"Fibonacci of 10: {fib(10)}")
print(f"Fibonacci of 15: {fib(15)}")
