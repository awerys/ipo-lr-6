#Вариант - 1 
import random
def generate_random_list():
    """Генерирует список из 25 случайных целых чисел от -50 до 50"""
    return [random.randint(-50, 50) for _ in range(25)]
def analyze_list(numbers):
    """Анализирует список и возвращает статистику"""
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
    """Выводит результаты анализа"""
    print("=" * 60)
    print("СГЕНЕРИРОВАННЫЙ СПИСОК:")
    print(numbers)
    print("=" * 60)
    print("\nСТАТИСТИКА:")
    print("-" * 40)
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
    """Версия с более подробным анализом"""
    # Генерация списка
    numbers = [random.randint(-50, 50) for _ in range(25)]
    print("ГЕНЕРИРОВАННЫЙ СПИСОК (25 элементов от -50 до 50):")
    print("Список:", numbers)
    print("\n" + "="*50)
    # Подсчет с использованием фильтрации
    positive_count = len([x for x in numbers if x > 0])
    negative_count = len([x for x in numbers if x < 0])
    zero_count = len([x for x in numbers if x == 0])
    total = len(numbers)
    # Вычисление процентов
    pos_percent = (positive_count / total) * 100
    neg_percent = (negative_count / total) * 100
    zero_percent = (zero_count / total) * 100
    print("АНАЛИЗ СПИСКА:")
    print(f"Положительные числа: {positive_count} шт. ({pos_percent:.1f}%)")
    print(f"Отрицательные числа: {negative_count} шт. ({neg_percent:.1f}%)")
    print(f"Нулевые значения:    {zero_count} шт. ({zero_percent:.1f}%)")
    print("\nЭКСТРЕМАЛЬНЫЕ ЗНАЧЕНИЯ:")
    print(f"Самое маленькое значение: {min(numbers)}")
    print(f"Самое большое значение:  {max(numbers)}")
    # Дополнительная информация
    print("\nДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ:")
    print(f"Диапазон значений: от {min(numbers)} до {max(numbers)}")
    print(f"Размах данных: {max(numbers) - min(numbers)}")
# Запуск программы
if __name__ == "__main__":
    print("ПРОГРАММА АНАЛИЗА СЛУЧАЙНОГО СПИСКА ЧИСЕЛ")
    print("=" * 50)
    # Можно выбрать любую версию:
    main()  # Основная версия
    # detailed_analysis()  # Детальная версия
    # Дополнительно: несколько запусков для демонстрации
    print("\n" + "="*50)
    print("ДОПОЛНИТЕЛЬНЫЙ ЗАПУСК:")
    detailed_analysis()
