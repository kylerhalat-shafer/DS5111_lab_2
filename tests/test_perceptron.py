import pytest
import sys
import unittest
import os
import platform
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
    def test_perceptron_failure(self):
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

    @pytest.mark.skipif(platform.system() != "Linux" or "ubuntu" not in platform.version().lower(), reason="Test runs only on Linux Ubuntu.")
    def test_os_specific_logic(self):
        # Fetch memory details using os.popen()
        total_memory, used_memory, free_memory = map(
            int, os.popen('free -t -m').readlines()[-1].split()[1:])
        min_memory = 100  # Example: 100MB 
        # Assert that the total_memory is greater than or equal to the min_memory
        self.assertGreaterEqual(total_memory, min_memory, f"Expected at least {min_memory/1000} GB of memory. Found only {total_memory/1000} GB.")
        # You can set desired thresholds for used_memory and free_memory if needed
        min_used_memory = 100  # Example: 100MB
        self.assertGreaterEqual(used_memory, min_used_memory, f"Expected at least {min_used_memory/1000} GB of used memory. Found only {used_memory/1000} GB.")
        min_free_memory = 100  # Example: 100MB
        self.assertGreaterEqual(free_memory, min_free_memory, f"Expected at least {min_free_memory/1000} GB of free memory. Found only {free_memory/1000} GB.")

    @pytest.mark.skip(reason="This test is not yet ready for prime time.")
    def test_not_ready(self):
        print("This won't be printed!")
        banana = "yellow"
        apple = "red"
        self.assertEqual(banana, apple, "Fruits are not the same!")

if __name__ == "__main__":
    unittest.main()

