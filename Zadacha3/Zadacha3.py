# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def get_input():
    while True:
        try:
            a = float(input('введите вещественное число : '))
            return str(a)
        except ValueError:
            print("Ошибочный ввод.")


# удаление  ' , ' в вещественном числе
str_a = get_input().replace('.', '')
# преобразование введеного числа в список целых чисел

s = sum(map(int, list(str_a)))

print(f'сумма цифр введенного числа: {s}')
