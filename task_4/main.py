def download_file_if_needed():
    import os
    import urllib.request
    filename = "text.txt"
    if not os.path.exists(filename):
            print("Скачивание")
            url = "https://prod-files-secure.s3.us-west-2.amazonaws.com/d9fc6719-e1f9-49a0-8e26-8e1860bb2010/5284659f-3402-4df2-94b5-ae272f5b7c15/text.txt"
            urllib.request.urlretrieve(url, filename)
            print("Файл скачан")
    return filename
def read_file_lines(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.readlines()
def search_strings(lines, search_term):
    found_lines = []
    for line_num, line in enumerate(lines, 1):
        # Убираем лишние пробелы и проверяем наличие подстроки
        clean_line = line.strip()
        if search_term.lower() in clean_line.lower():
            found_lines.append((line_num, clean_line))
    return found_lines
def sort_lines_by_length(lines):
     return sorted(lines, key=lambda x: len(x[1]))
def main():
    filename = download_file_if_needed()
    # Читаем строки из файла
    lines = read_file_lines(filename)
    if lines is None:
        return
    print(f"Файл '{filename}'  загружен. Всего строк: {len(lines)}")
    # Запрашиваем строку для поиска
    search_term = input("Введите строку для поиска: ").strip()
    # Ищем строки, содержащие искомую подстроку
    found_lines = search_strings(lines, search_term)
    # Выводим результаты поиска
    print(f"\nРезультаты поиска подстроки '{search_term}':")
    print(f"Найдено строк: {len(found_lines)}")
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
