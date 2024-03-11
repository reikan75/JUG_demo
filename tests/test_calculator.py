from unittest import TestCase
from src.calculator import Calculator

class Test_Calculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        self.assertEqual(self.calc.mysum(1, 2), 3)

    def test_min(self):
        self.assertEqual(self.calc.mymin(1, 2), 1)

    
    
if __name__ == '__main__':
    unittest.main()