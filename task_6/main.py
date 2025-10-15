#Вариант - 1 
import random
import itertools
def generate_random_lists():
    """Создает случайный список из 20 значений по 4 случайных целых чисел от -10 до 10"""
    main_list = []
    for _ in range(20):
        sublist = [random.randint(-10, 10) for _ in range(4)]
        main_list.append(sublist)
    return main_list
def find_unique_combinations(main_list):
    """Находит все уникальные комбинации (без учета порядка)"""
    unique_combinations = set()
    for sublist in main_list:
        # Сортируем подсписок и преобразуем в кортеж для уникальности
        sorted_sublist = sorted(sublist)
        unique_combinations.add(tuple(sorted_sublist))
    return list(unique_combinations)
def count_pairs_with_sum_less_than(unique_combinations, target_sum):
    """Вычисляет количество пар, чья сумма меньше заданного значения"""
    count = 0
    pairs = []
    # Перебираем все пары уникальных комбинаций
    for i in range(len(unique_combinations)):
        for j in range(i + 1, len(unique_combinations)):
            # Суммируем все элементы обеих комбинаций
            total_sum = sum(unique_combinations[i]) + sum(unique_combinations[j])
            if total_sum < target_sum:
                count += 1
                pairs.append((unique_combinations[i], unique_combinations[j], total_sum))
    return count, pairs
def main():
    # Создаем случайный список
    main_list = generate_random_lists()
    print("СЛУЧАЙНЫЙ СПИСОК ИЗ 20 ПОДСПИСКОВ ПО 4 ЭЛЕМЕНТА:")
    print("=" * 60)
    for i, sublist in enumerate(main_list, 1):
        print(f"Список {i:2}: {sublist} (сумма: {sum(sublist)})")
    # Находим уникальные комбинации
    unique_combinations = find_unique_combinations(main_list)
    print(f"\nУНИКАЛЬНЫЕ КОМБИНАЦИИ (всего {len(unique_combinations)}):")
    print("=" * 60)
    for i, combo in enumerate(unique_combinations, 1):
        print(f"Комбинация {i:2}: {combo} (сумма: {sum(combo)})")
    # Пользователь вводит число
    print("\n" + "=" * 60)
    try:
        target_number = int(input("Введите целое число для сравнения сумм пар: "))
    except ValueError:
        print("Ошибка! Введите целое число.")
        return
    # Вычисляем количество пар с суммой меньше заданного значения
    pairs_count, pairs_list = count_pairs_with_sum_less_than(unique_combinations, target_number)
    print(f"\nРЕЗУЛЬТАТЫ ДЛЯ ЧИСЛА {target_number}:")
    print("=" * 60)
    print(f"Количество пар, чья сумма меньше {target_number}: {pairs_count}")
    if pairs_count > 0:
        print(f"\nНайденные пары (сумма < {target_number}):")
        for i, (combo1, combo2, total_sum) in enumerate(pairs_list, 1):
            print(f"Пара {i:2}: {combo1} + {combo2} = {total_sum}")
# Альтернативная версия с использованием itertools.combinations
def alternative_version():
    """Альтернативная версия с использованием itertools"""
    # Генерация списка
    main_list = [[random.randint(-10, 10) for _ in range(4)] for _ in range(20)]
    print("АЛЬТЕРНАТИВНАЯ ВЕРСИЯ:")
    print("Сгенерированный список:")
    for i, sublist in enumerate(main_list, 1):
        print(f"{i:2}: {sublist}")
    # Уникальные комбинации
    unique_combos = set(tuple(sorted(sublist)) for sublist in main_list)
    unique_combos_list = list(unique_combos)
    print(f"\nУникальные комбинации ({len(unique_combos_list)} шт.):")
    for combo in unique_combos_list:
        print(f"  {combo}")
    # Ввод числа пользователем
    try:
        user_number = int(input("\nВведите целое число: "))
    except ValueError:
        print("Некорректный ввод!")
        return
    # Подсчет пар с помощью itertools
    pairs_count = 0
    print(f"\nПары с суммой меньше {user_number}:")
    # Генерируем все возможные пары уникальных комбинаций
    for combo1, combo2 in itertools.combinations(unique_combos_list, 2):
        total_sum = sum(combo1) + sum(combo2)
        if total_sum < user_number:
            pairs_count += 1
            print(f"  {combo1} + {combo2} = {total_sum}")
    print(f"\nИтого: {pairs_count} пар(ы)")
# Упрощенная версия для быстрого тестирования
def simple_version():
    """Упрощенная версия программы"""
    # Генерация
    data = [[random.randint(-10, 10) for _ in range(4)] for _ in range(20)]
    print("УПРОЩЕННАЯ ВЕРСИЯ")
    print(f"Сгенерировано: 20 списков по 4 числа")
    # Уникальные комбинации
    unique = list(set(tuple(sorted(lst)) for lst in data))
    print(f"Уникальных комбинаций: {len(unique)}")
    # Ввод числа
    try:
        n = int(input("Введите число: "))
    except:
        print("Ошибка ввода!")
        return
    # Подсчет пар
    count = 0
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if sum(unique[i]) + sum(unique[j]) < n:
                count += 1
    print(f"Пар с суммой меньше {n}: {count}")
if __name__ == "__main__":
    print("ПРОГРАММА АНАЛИЗА СЛУЧАЙНЫХ КОМБИНАЦИЙ")
    print("=" * 60)
    # Выберите версию для запуска:
    main()  # Основная версия с подробным выводом
    # alternative_version()  # Альтернативная версия с itertools
    # simple_version()  # Упрощенная версия
