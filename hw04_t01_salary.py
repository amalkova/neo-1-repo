#Завдання 1 - total_salary(path) = загальна та середня сума заробітної плати

def create_test_salary_file():
    content = """Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
InvalidLineWithoutComma
Michael Johnson,abc
"""
    with open("salary_file.txt", "w", encoding="utf-8") as file:
        file.write(content)

def total_salary(path):
    try:
        #Використовуйте менеджер контексту with для читання файлів.
        #Пам'ятайте про встановлення кодування при відкриті файлів
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                #Для розділення даних у кожному рядку можна застосувати метод split(',').
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        salary = float(parts[1])
                        salaries.append(salary)
                    except ValueError:
                        # Якщо зарплата не число — пропускаємо рядок
                        continue
            if not salaries:
                return 0, 0
            #Обрахуйте загальну суму заробітної плати, а потім розділіть її на кількість розробників, щоб отримати середню зарплату.
            total = sum(salaries)
            average = total / len(salaries)
            return total, average
    #Опрацьовуйте можливі винятки при роботі з файлами, такі як відсутність файлу.
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0