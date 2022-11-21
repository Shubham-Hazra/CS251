import unittest
import polygon_land

class TestAlgo(unittest.TestCase):
    def testminCost_triangle(self):
        values = [1, 2, 3]
        self.assertEqual(polygon_land.minCost(values), 6)

    def testminCost_square(self):
        values = [5, 3, 7, 4]
        self.assertEqual(polygon_land.minCost(values), 144)

    def testminCost_hexagon(self):
        values = [1, 3, 1, 4, 1, 5]
        self.assertEqual(polygon_land.minCost(values), 13)

if __name__ == '__main__':
	unittest.main()