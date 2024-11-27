import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_negative_area(self):
        with self.assertRaises(Exception) as context:
            area(-1, 3)
        self.assertTrue(context.exception)

    def test_area(self):
        res = area(5, 2)
        self.assertEqual(res, 10)
    
    def test_zero_perimeter(self):
        res = perimeter(0, 4)
        self.assertEqual(res, 0)

    def test_negative_perimeter(self):
        with self.assertRaises(Exception) as context:
            perimeter(-1, 4)
        self.assertTrue(context.exception)   

    def test_perimeter(self):
        res = perimeter(4, 5)
        self.assertEqual(res, 18)


def area(a, b):
    ''' Возвращает площадь прямоугольника
            Параметры:
                a (number): первая сторона прямоугольника
                b (number): вторая сторона прямоугольника
            Возвращаемое значение:
                area (number): площадь прямоугольника
    '''

    if(a < 0 or b < 0):
        raise Exception("Сторона не может быть отрицательной")

    return a * b

def perimeter(a, b):
    ''' Возвращает периметр прямоугольника
            Параметры:
                a (number): первая сторона прямоугольника
                b (number): вторая сторона прямоугольника
            Возвращаемое значение:
                perimeter (number): периметр прямоугольника
    '''

    if(a < 0 or b < 0):
        raise Exception("Сторона не может быть отрицательной")
    
    if (a == 0 or b == 0):
        return 0

    return a * 2 + b * 2
