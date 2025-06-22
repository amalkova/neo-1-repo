#Завдання 3 - структура папок
#Спочатку встановіть бібліотеку colorama. Для цього створіть та активуйте віртуальне оточення Python, а потім встановіть пакет за допомогою pip.

#Для роботи з файловою системою використовуйте модуль pathlib.
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)


IGNORE_NAMES = {'.DS_Store', 'venv'}

def print_directory_structure(path: Path, indent_level=0):
    try:
        for item in sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower())):
            if item.name in IGNORE_NAMES:
                continue

            indent = "    " * indent_level
            if item.is_dir():
                print(f"{indent}{Fore.CYAN}{item.name}/")
                print_directory_structure(item, indent_level + 1)
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{Fore.RED}Permission denied: {path}")

def validate_directory_path(directory_path: Path):
    if not directory_path.exists():
        raise FileNotFoundError(f"Директорія {directory_path} не існує.")
    if not directory_path.is_dir():
        raise NotADirectoryError(f"Шлях {directory_path} не є директорією.")