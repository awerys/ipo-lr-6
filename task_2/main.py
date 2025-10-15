#Вариант - 1 
import random
def create_matrix():
    # Заданный список значений
    values = [-3, -5, -2, -12, 0, 15, 4, 7, 2]
    # Генерируем случайный размер матрицы от 4 до 8
    size = random.randint(4, 8)
    # Создаем матрицу, заполняя случайными значениями из списка
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(random.choice(values))
        matrix.append(row)
    return matrix
def print_matrix(matrix):
    # Выводим матрицу в форматированном виде
    for row in matrix:
        # Форматируем каждое число с выравниванием
        formatted_row = [f"{num:3}" for num in row]
        print(" ".join(formatted_row))
def main():
    # Создаем матрицу
    matrix = create_matrix()
    # Выводим информацию о размере
    print(f"Матрица размером {len(matrix)}x{len(matrix)}:")
    print()
    # Выводим матрицу
    print_matrix(matrix)
    # Дополнительная информация
    print(f"\nИспользованные значения: [-3, -5, -2, -12, 0, 15, 4, 7, 2]")
# Запускаем программу
if __name__ == "__main__":
    main()
