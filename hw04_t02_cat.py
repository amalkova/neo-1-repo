#Завдання 2 - get_cats_info(path) = список словників з інформацією про кожного кота

#Функція для створення тестового файлу з інформацією про котів
#Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
def create_test_cats_file():
    content = """60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
"""
    with open("cats_file.txt", "w", encoding="utf-8") as file:
        file.write(content)
    print("Файл cats_file.txt успішно створено.")

#Функція для читання файлу і формування списку словників з інформацією про котів
def get_cats_info(path):
    cats_list = []
    try:
        #Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_dict = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    #Функція має повертати список словників, де кожен словник містить інформацію про одного кота.
                    cats_list.append(cat_dict)
        return cats_list
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []