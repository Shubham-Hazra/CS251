import unittest
import polygon_land

class TestAlgo(unittest.TestCase):
    def testminCost_triangle(self):
        values = [1, 2, 3]
        returned_value = polygon_land.minCost(values)
        message = "\n test case = [1, 2, 3] Expected output = 6 Returned output = " + str(returned_value)
        self.assertEqual(returned_value, 6, message)

    def testminCost_square(self):
        values = [5, 3, 7, 4]
        returned_value = polygon_land.minCost(values)
        message = "\n test case = [5, 3, 7, 4] Expected output = 144 Returned output = " + str(returned_value)
        self.assertEqual(returned_value, 144, message)

    def testminCost_hexagon(self):
        values = [1, 3, 1, 4, 1, 5]
        returned_value = polygon_land.minCost(values)
        message = "\n test case = [1, 3, 1, 4, 1, 5] Expected output = 13 Returned output = " + str(returned_value)
        self.assertEqual(returned_value, 13, message)

    def testminCost_pentagon(self):
        values = [5, 10, 5, 2, 1]
        returned_value = polygon_land.minCost(values)
        message = "\n test case = [5, 10, 5, 2, 1] Expected output = 110 Returned output = " + str(returned_value)
        self.assertEqual(returned_value, 110, message)

    def testminCost_maxCapacity(self):
        values = [1, 5, 3, 2, 6, 7, 8, 1, 7, 1]
        returned_value = polygon_land.minCost(values)
        message = "\n test case = [1, 5, 3, 2, 6, 7, 8, 1, 7, 1] Expected output = 141 Returned output = " + str(returned_value)
        self.assertEqual(returned_value, 141, message)

if __name__ == '__main__':
    unittest.main()