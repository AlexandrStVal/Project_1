# HomeWork 16.9.1
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
# магичесикй метод для отображения информации об объекте класса
# для пользователя
    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}.'

rect = Rectangle(5, 10, 50, 100)
print(rect)
print('_____________')

# HomeWork 16.9.2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print(f'Площадь прямоугольника: {rect.getArea()}')
print('_____________')

# HomeWork 16.9.3 и
class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."'

client_1 = Client('Иван', 'Петров', 'Москва', 50)
client_2 = Client('Захар', 'Гаврилов', 'Кемерово', 100)

clients = [client_1, client_2]
for client in clients:
    print(client)
print('_____________')

# HomeWork 16.9.4
class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."'

    def listCorp(self):
        return f'"{self.name} {self.surname}. {self.city}."'

client_1 = Client('Иван', 'Петров', 'Москва', 50)
client_2 = Client('Захар', 'Гаврилов', 'Кемерово', 100)

clients = [client_1, client_2]
# for client in clients:
#     print(client)
# print('____________')

for client in clients:  # Список без баланса
    print(client.listCorp())