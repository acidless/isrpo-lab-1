import math
import unittest

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_negative_area(self):
        with self.assertRaises(Exception) as context:
            area(-1)
        self.assertTrue(context.exception)

    def test_area(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.54, places=2)
    
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_negative_perimeter(self):
        with self.assertRaises(Exception) as context:
            perimeter(-1)
        self.assertTrue(context.exception)   

    def test_perimeter(self):
        res = perimeter(4)
        self.assertAlmostEqual(res, 25.13, places=2)


def area(r):
    ''' Возвращает площадь круга 
            Параметры:
                r (number): радиус круга
            Возвращаемое значение:
                area (number): площадь круга
    '''

    if(r < 0):
        raise Exception("Радиус не может быть отрицательным")

    return math.pi * r * r


def perimeter(r):
    ''' Возвращает периметр круга 
            Параметры:
                r (number): радиус круга
            Возвращаемое значение:
                perimeter (number): периметр
    '''

    if(r < 0):
        raise Exception("Радиус не может быть отрицательным")

    return 2 * math.pi * r

