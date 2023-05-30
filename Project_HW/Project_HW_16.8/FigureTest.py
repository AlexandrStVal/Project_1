from FigureClass import Rectangle, Square, Circle

# создаем два прямоугольника
rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
# выводим площади наших двух прямоугольников
print('rect_1:', rect_1.getArea(), '\n'
      'rect_2:', rect_2.getArea())

square_1 = Square(5)
square_2 = Square(10)
print('square_1:', square_1.getAreaSquare(), '\n' 
      'square_2:', square_2.getAreaSquare())

circle_1 = Circle(5)
circle_2 = Circle(10)
print('circle_1:', circle_1.getAreaCircle(), '\n' 
      'circle_2:', circle_2.getAreaCircle())

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    ''' В условии есть функция isinstance, поддерживающая наследование.
Она проверяет, является ли аргумент объекта экземпляром класса или
экземпляром класса из кортежа. В случае если является, функция возвращает True,
если не является — False.'''
    if isinstance(figure, Square):
        print(f'square: {figure.getAreaSquare()}')
    elif isinstance(figure, Circle):
        print(f'circle: {figure.getAreaCircle()}')
    else:
        print(f'rect: {figure.getArea()}')