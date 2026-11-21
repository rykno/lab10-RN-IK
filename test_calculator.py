import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(5, add(5, 5), "Function error!" )

    def test_subtract(self): # 3 assertions
        self.assertEqual(10, sub(15, 5), "Function error!")


    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertEqual("Cannot divide by zero", div(0, 5),"Function error!")
        self.assertEqual(15, div(15,225), "Function error!")

    def test_logarithm(self): # 3 assertions
        self.assertEqual(2, log(3, 9), "Function error!")
        self.assertEqual("Invalid input for logarithm", log(5, 0), "Function error!")
        self.assertEqual("Invalid input for logarithm", log(2, -2), "Function error!")



    def test_log_invalid_base(self): # 1 assertion
        self.assertEqual("Invalid input for logarithm", log(0, 5), "Function error!")
        self.assertEqual("Invalid input for logarithm", log(-2, 5), "Function error!")
        self.assertEqual("Invalid input for logarithm", log(1, 5), "Function error!")
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()