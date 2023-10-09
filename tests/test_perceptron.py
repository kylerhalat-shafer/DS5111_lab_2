import pytest
import sys
import unittest
sys.path.append("..")

from bin.perceptron_module import Perceptron

class TestPerceptron(unittest.TestCase):

    def test_perceptron_logic(self):
        the_perceptron = Perceptron()
        the_perceptron.train([
            [1,1],
            [1,0],
            [0,1],
            [0,0],
        ], [1,1,1,0])

        self.assertEqual(the_perceptron.predict([1,1]), 1, "Expected 1 for input [1,1]")
        self.assertEqual(the_perceptron.predict([1,0]), 1, "Expected 1 for input [1,0]")
        self.assertEqual(the_perceptron.predict([0,1]), 1, "Expected 1 for input [0,1]")
        self.assertEqual(the_perceptron.predict([0,0]), 0, "Expected 0 for input [0,0]")

    @pytest.mark.xfail(reason="this test is expected to fail.")
    def test_perceptron_logic(self):
        the_perceptron = Perceptron()
        the_perceptron.train([
            [1,1],
            [1,0],
            [0,1],
            [0,0],
        ], [1,1,1,0])

        self.assertNotEqual(the_perceptron.predict([1,1]), 1, "Expected failure for input [1,1]")
        self.assertEqual(the_perceptron.predict([1,0]), 1, "Expected 1 for input [1,0]")
        self.assertEqual(the_perceptron.predict([0,1]), 1, "Expected 1 for input [0,1]")
        self.assertEqual(the_perceptron.predict([0,0]), 0, "Expected 0 for input [0,0]")

if __name__ == "__main__":
    unittest.main()

