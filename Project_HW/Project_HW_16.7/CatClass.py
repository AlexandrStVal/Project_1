class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f'Имя котофея: {self.name}, пол: {self.gender}, возраст: {self.age}'
