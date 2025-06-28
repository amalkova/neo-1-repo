#Завдання 1 - caching_fibonacci

def caching_fibonacci():
    # Функція повертає функцію для обчислення чисел Фібоначчі з кешуванням
    
    cache = {}

    def fibonacci(n):
        # Обчислює n-те число Фібоначчі з використанням кешу
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci