#https://github.com/rykno/lab10-RN-IK.git
#Partner 1:Ryan Nguyen
#Partner 2:Ishaan Krishna

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(5, add(5, 5), "Function error!" )

    def test_subtract(self): # 3 assertions
        self.assertEqual(10, subtract(15, 5), "Function error!")


    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5,4),20)
        self.assertEqual(mul(-2,3),6)
        self.assertEqual(mul(0,5),0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10,2),5)
        self.assertAlmostEqual(div(7,3),2.3333333)
        self.assertEqual(div(-10,2),-5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertEqual("Cannot divide by zero", div(0, 5),"Function error!")
        self.assertEqual(15, div(15,225), "Function error!")

    def test_logarithm(self): # 3 assertions
        self.assertEqual(2, logarithm(3, 9), "Function error!")
        self.assertEqual("Invalid input for logarithm", logarithm(5, 0), "Function error!")
        self.assertEqual("Invalid input for logarithm", logarithm(2, -2), "Function error!")



    def test_log_invalid_base(self): # 1 assertion
        self.assertEqual("Invalid input for logarithm", logarithm(0, 5), "Function error!")
        self.assertEqual("Invalid input for logarithm", logarithm(-2, 5), "Function error!")
        self.assertEqual("Invalid input for logarithm", logarithm(1, 5), "Function error!")
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(5,12),13)
        self.assertEqual(hypotenuse(8,15),17)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(25),5)
        self.assertEqual(square_root(0),0)
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()