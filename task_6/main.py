#Вариант - 1 
import random
import itertools
def generate_random_lists():
    main_list = []
    for _ in range(20):
        sublist = [random.randint(-10, 10) for _ in range(4)]
        main_list.append(sublist)
    return main_list
def find_unique_combinations(main_list):
    unique_combinations = set()
    for sublist in main_list:
        # Сортируем подсписок и преобразуем в кортеж для уникальности
        sorted_sublist = sorted(sublist)
        unique_combinations.add(tuple(sorted_sublist))
    return list(unique_combinations)
def count_pairs_with_sum_less_than(unique_combinations, target_sum):
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
    print("Случайный список:")
    for i, sublist in enumerate(main_list, 1):
        print(f"Список {i:2}: {sublist} (сумма: {sum(sublist)})")
    # Находим уникальные комбинации
    unique_combinations = find_unique_combinations(main_list)
    print(f"\nУникальные комбинации (всего {len(unique_combinations)}):")
    print("=" * 60)
    for i, combo in enumerate(unique_combinations, 1):
        print(f"Комбинация {i:2}: {combo} (сумма: {sum(combo)})")
    # Пользователь вводит число
    print("\n")
        target_number = int(input("Введите целое число для сравнения сумм пар: "))
    # Вычисляем количество пар с суммой меньше заданного значения
    pairs_count, pairs_list = count_pairs_with_sum_less_than(unique_combinations, target_number)
    print(f"\nРезультаты {target_number}:")
    print(f"Количество пар, чья сумма меньше {target_number}: {pairs_count}")
    if pairs_count > 0:
        print(f"\nНайденные пары (сумма < {target_number}):")
        for i, (combo1, combo2, total_sum) in enumerate(pairs_list, 1):
            print(f"Пара {i:2}: {combo1} + {combo2} = {total_sum}")
