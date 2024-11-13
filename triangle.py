import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_negative_area(self):
        with self.assertRaises(Exception) as context:
            area(10, -1)
        self.assertTrue(context.exception)

    def test_area(self):
        res = area(5, 4)
        self.assertEqual(res, 10)
    
    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_negative_perimeter(self):
        with self.assertRaises(Exception) as context:
            perimeter(-1, 0, 0)
        self.assertTrue(context.exception)   

    def test_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
       


def area(a, h):
    ''' Возвращает площадь треугольника
            Параметры:
                a (number): сторона треугольника
                h (number): высота, проведенная к этой стороне
            Возвращаемое значение:
                area (number): площадь треугольника
    '''

    if(a < 0 or h < 0):
        raise Exception("Сторона не может быть отрицательной")

    return a * h / 2

def perimeter(a, b, c):
    ''' Возвращает периметр треугольника
            Параметры:
                a (number): первая сторона треугольника
                b (number): вторая сторона треугольника
                c (number): третья сторона треугольника
            Возвращаемое значение:
                perimeter (number): периметр треугольника
    '''
    if(a < 0 or b < 0 or c < 0):
        raise Exception("Сторона не может быть отрицательной")

    return a + b + c