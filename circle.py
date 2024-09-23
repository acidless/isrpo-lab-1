import math


def area(r):
    ''' Возвращает площадь круга 
            Параметры:
                r (number): радиус круга
            Возвращаемое значение:
                area (number): площадь круга
    '''

    return math.pi * r * r


def perimeter(r):
    ''' Возвращает периметр круга 
            Параметры:
                r (number): радиус круга
            Возвращаемое значение:
                perimeter (number): периметр
    '''

    return 2 * math.pi * r

