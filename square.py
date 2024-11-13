import unittest

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_negative_area(self):
        with self.assertRaises(Exception) as context:
            area(-1)
        self.assertTrue(context.exception)

    def test_area(self):
        res = area(5)
        self.assertEqual(res, 25)
    
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_negative_perimeter(self):
        with self.assertRaises(Exception) as context:
            perimeter(-1)
        self.assertTrue(context.exception)   

    def test_perimeter(self):
        res = perimeter(3)
        self.assertEqual(res, 12)


def area(a):
    ''' Возвращает площадь квадрата
            Параметры:
                a (number): сторона квадрата
            Возвращаемое значение:
                area (number): площадь квадрата
    '''

    if(a < 0):
        raise Exception("Сторона не может быть отрицательной")

    return a * a


def perimeter(a):
    ''' Возвращает периметр квадрата
            Параметры:
                a (number): сторона квадрата
            Возвращаемое значение:
                perimeter (number): периметр квадрата
    '''

    if(a < 0):
        raise Exception("Сторона не может быть отрицательной")

    return 4 * a
