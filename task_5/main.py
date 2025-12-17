#Вариант - 1 
import random
def generate_random_list():
    return [random.randint(-50, 50) for _ in range(25)]
def analyze_list(numbers):
    total = len(numbers)
    # Подсчет положительных, отрицательных и нулевых элементов
    positive = [x for x in numbers if x > 0]
    negative = [x for x in numbers if x < 0]
    zero = [x for x in numbers if x == 0]
    # Расчет процентов
    positive_percent = (len(positive) / total) * 100
    negative_percent = (len(negative) / total) * 100
    zero_percent = (len(zero) / total) * 100
    # Нахождение минимального и максимального значения
    min_value = min(numbers)
    max_value = max(numbers)
    return {
        'positive': (positive, positive_percent),
        'negative': (negative, negative_percent),
        'zero': (zero, zero_percent),
        'min': min_value,
        'max': max_value,
        'total': total
    }
def print_results(numbers, stats):
    print("Получившейся список:")
    print(numbers)
    print("\nСтатистика:")
    # Положительные числа
    pos_list, pos_percent = stats['positive']
    print(f"Положительные элементы: {len(pos_list)} ({pos_percent:.1f}%)")
    if pos_list:
        print(f"  Значения: {pos_list}")
    # Отрицательные числа
    neg_list, neg_percent = stats['negative']
    print(f"Отрицательные элементы: {len(neg_list)} ({neg_percent:.1f}%)")
    if neg_list:
        print(f"  Значения: {neg_list}")
    # Нулевые элементы
    zero_list, zero_percent = stats['zero']
    print(f"Нулевые элементы: {len(zero_list)} ({zero_percent:.1f}%)")
    if zero_list:
        print(f"  Значения: {zero_list}")
    print("-" * 40)
    print(f"Минимальное значение: {stats['min']}")
    print(f"Максимальное значение: {stats['max']}")
    print(f"Общее количество элементов: {stats['total']}")
def main():
    # Генерируем список случайных чисел
    random_numbers = generate_random_list()
    # Анализируем список
    statistics = analyze_list(random_numbers)
    # Выводим результаты
    print_results(random_numbers, statistics)
# Альтернативная версия с более детальным анализом
def detailed_analysis():
    # Генерация списка
    numbers = [random.randint(-50, 50) for _ in range(25)]
    print("Получившийся список:")
    print("Список:", numbers)
    print("\n")
    # Подсчет с использованием фильтрации
    positive_count = len([x for x in numbers if x > 0])
    negative_count = len([x for x in numbers if x < 0])
    zero_count = len([x for x in numbers if x == 0])
    total = len(numbers)
    # Вычисление процентов
    pos_percent = (positive_count / total) * 100
    neg_percent = (negative_count / total) * 100
    zero_percent = (zero_count / total) * 100
    print("Анализ списка:")
    print(f"Положительные числа: {positive_count} шт. ({pos_percent:.1f}%)")
    print(f"Отрицательные числа: {negative_count} шт. ({neg_percent:.1f}%)")
    print(f"Нулевые значения:    {zero_count} шт. ({zero_percent:.1f}%)")
    print("\nЗначения:")
    print(f"Самое маленькое: {min(numbers)}")
    print(f"Самое большое:  {max(numbers)}")
    # Дополнительная информация
    print("\nДополнительная инфа:")
    print(f"Диапазон: от {min(numbers)} до {max(numbers)}")
    print(f"Размах данных: {max(numbers) - min(numbers)}")
# Запуск программы
if __name__ == "__main__":
    print("Анализ списка")
