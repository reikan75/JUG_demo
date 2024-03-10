from unittest import TestCase
from src.calculator import Calculator

class Test_Calculator(TestCase):
    def test_sum(self):
        calc = Calculator()
        self.assertEqual(calc.mysum(1, 2), 3)
    
if __name__ == '__main__':
    unittest.main()