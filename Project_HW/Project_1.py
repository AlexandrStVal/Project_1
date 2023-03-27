try:
    money = int(input('Введите сумму вклада (руб.): '))  # 100000
except ValueError:
    print("Введен некорректный формат!")
    money = int(input('Введите сумму вклада в формате цифр (руб.): '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
percent_list = list(per_cent.values())
deposit = []  # [5600, 5900, 4280, 4000]
for i in range(0, len(percent_list)):
    deposit.append(round(percent_list[i] * money / 100))
max_deposit = max(deposit)
print(f'deposit = {deposit}')
print(f'Максимальная сумма, которую вы можете заработать — {max_deposit:.2f} руб.')
# print('Максимальная сумма, которую вы можете заработать — %.0f' % (max_deposit), 'руб.')