#Вариант - 1 
def get_number_of_lines():
    while True:
        try:
            n = int(input("Введите количество строк: "))
                continue
            return n
def get_lines(n):
    lines = []
    print(f"\nВведите {n} строк:")
    for i in range(n):
        line = input(f"Строка {i + 1}: ")
        lines.append(line)
    return lines
def count_unique_words(lines):
    all_words = []
    for line in lines:
        # Разбиваем строку на слова (последовательности непробельных символов)
        words = line.split()
        all_words.extend(words)
    # Создаем множество для получения уникальных слов
    unique_words = set(all_words)
    return len(unique_words), unique_words
def main():
    # Запрашиваем количество строк с проверкой
    n = get_number_of_lines()
    # Запрашиваем сами строки
    lines = get_lines(n)
    # Подсчитываем количество различных слов
    unique_count, unique_words = count_unique_words(lines)
    # Выводим результаты
    print(f"\nРезультаты:")
    print(f"Всего строк: {n}")
    print(f"Количество различных слов: {unique_count}")
    # Дополнительно: вывод списка уникальных слов (по желанию)
    print(f"\nУникальные слова: {', '.join(sorted(unique_words))}")
# Запускаем программу
if __name__ == "__main__":
    main()
