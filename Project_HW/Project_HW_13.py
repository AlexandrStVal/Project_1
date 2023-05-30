tickets = int(input('Введите количество билетов: '))  # 4
age = [int(input('Введите возраст посетителя: ')) for i in range(tickets)]  # [18, 25, 33, 45]
prices = 0
print('_______')
for item in age:
    if item < 18:
        print('Вход на конференцию бесплатно:', item, 'лет')
    elif 18 <= item < 25:
        prices += 990
        print('Стоимость входа на конференцию 990 руб.:', item, 'лет')
    else:
        prices += 1390
        print('Стоимость входа на конференцию 1390 руб.:', item, 'лет/года')
print('________')
if tickets > 3:
    prices = prices - ((prices /100) * 10)
    print(f'Общая стоимость входа на конференцию, с учетом скидки 10 %: {prices:.2f} руб.')  # 4644.00 руб.
else:
    print(f'Общая стоимость входа на конференцию: {prices:.2f} руб.')