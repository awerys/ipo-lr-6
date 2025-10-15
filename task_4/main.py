def download_file_if_needed():
    """Скачивает файл, если он отсутствует"""
    import os
    import urllib.request
    filename = "text.txt"
    if not os.path.exists(filename):
        try:
            print("Скачиваю файл text.txt...")
            url = "https://prod-files-secure.s3.us-west-2.amazonaws.com/d9fc6719-e1f9-49a0-8e26-8e1860bb2010/5284659f-3402-4df2-94b5-ae272f5b7c15/text.txt"
            urllib.request.urlretrieve(url, filename)
            print("Файл успешно скачан!")
        except Exception as e:
            print(f"Ошибка при скачивании файла: {e}")
            return None
    return filename
def read_file_lines(filename):
    """Читает все строки из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None
def search_strings(lines, search_term):
    """Находит строки, содержащие искомую подстроку"""
    found_lines = []
    for line_num, line in enumerate(lines, 1):
        # Убираем лишние пробелы и проверяем наличие подстроки
        clean_line = line.strip()
        if search_term.lower() in clean_line.lower():
            found_lines.append((line_num, clean_line))
    return found_lines
def sort_lines_by_length(lines):
    """Сортирует строки по длине (от самой короткой к самой длинной)"""
    return sorted(lines, key=lambda x: len(x[1]))
def main():
    # Получаем файл (скачиваем если нужно)
    filename = download_file_if_needed()
    if not filename:
        print("Не удалось получить файл для работы.")
        return
    # Читаем строки из файла
    lines = read_file_lines(filename)
    if lines is None:
        return
    print(f"Файл '{filename}' успешно загружен. Всего строк: {len(lines)}")
    print("-" * 50)
    # Запрашиваем строку для поиска
    search_term = input("Введите строку для поиска: ").strip()
    if not search_term:
        print("Строка для поиска не может быть пустой!")
        return
    # Ищем строки, содержащие искомую подстроку
    found_lines = search_strings(lines, search_term)
    # Выводим результаты поиска
    print(f"\nРезультаты поиска подстроки '{search_term}':")
    print(f"Найдено строк: {len(found_lines)}")
    print("-" * 50)
    if found_lines:
        print("Все найденные строки:")
        for line_num, line in found_lines:
            print(f"Строка {line_num}: {line}")
        # Сортируем строки по длине
        sorted_lines = sort_lines_by_length(found_lines)
        print(f"\nОтсортированные строки (по длине, от короткой к длинной):")
        print("-" * 50)
        for line_num, line in sorted_lines:
            print(f"[Длина: {len(line):2}] Строка {line_num}: {line}")
    else:
        print("Строки с указанной подстрокой не найдены.")
# Альтернативная версия без скачивания (если файл уже есть)
def main_simple():
    """Упрощенная версия без скачивания"""
    filename = "text.txt"
    # Читаем строки из файла
    lines = read_file_lines(filename)
    if lines is None:
        return
    print(f"Файл '{filename}' загружен. Всего строк: {len(lines)}")
    print("-" * 50)
    # Запрашиваем строку для поиска
    search_term = input("Введите строку для поиска: ").strip()
    if not search_term:
        print("Строка для поиска не может быть пустой!")
        return
    # Ищем строки
    found_lines = search_strings(lines, search_term)
    # Выводим результаты
    print(f"\nРезультаты поиска '{search_term}':")
    print(f"Найдено строк: {len(found_lines)}")
    if found_lines:
        print("\nВсе найденные строки:")
        for line_num, line in found_lines:
            print(f"Строка {line_num}: {line}")
        # Сортируем по длине
        sorted_lines = sort_lines_by_length(found_lines)
        print(f"\nОтсортированные по длине:")
        for line_num, line in sorted_lines:
            print(f"[{len(line):2} симв.] Строка {line_num}: {line}")
    else:
        print("Ничего не найдено.")
if __name__ == "__main__":
    # Выберите одну из версий:
    main()       # С автоматическим скачиванием
    # main_simple()  # Без скачивания (если файл уже есть)
