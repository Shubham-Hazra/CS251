import unittest
import grader

class TestAlgo(unittest.TestCase):
    def testgrader_add1(self):
        self.assertEqual(grader.apply(grader.add, (2,3)), 5)
    
    def testgrader_add2(self):
        with self.assertRaises(Exception) :
            grader.add('a', 2)
    
    def testgrader_sub1(self):
        self.assertEqual(grader.apply(grader.subtract, (2,3)), -1)
    
    def testgrader_sub2(self):
        with self.assertRaises(Exception):
            grader.subtract(5, "a")
    
    def testgrader_div1(self):
        self.assertEqual(grader.apply(grader.divide, (2,3)), 2/3)
    
    def testgrader_div2(self):
        with self.assertRaises(Exception):
            grader.divide(5, 0)

    def testgrader_str_left_rotate1(self):
        self.assertEqual(grader.apply(grader.str_left_rotate, ("CS251", 2)), "251CS")
    
    def testgrader_str_left_rotate2(self):
        with self.assertRaises(Exception):
            grader.str_left_rotate("CS251", "a")

    def testgrader_str_left_rotate3(self):
        with self.assertRaises(Exception):
            grader.str_left_rotate(52, 2)
            


if __name__ == '__main__':
    unittest.main()