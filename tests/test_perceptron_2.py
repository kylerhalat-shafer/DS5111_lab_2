import sys
import os
import platform
sys.path.append("..")

import pytest
from bin.perceptron_module import Perceptron

@pytest.mark.parametrize("training_data, labels, expected_outputs", [
    # First dataset
    ([
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 0],
    ], [1, 1, 1, 0], [1, 1, 1, 0]),

    # Second dataset: AND logic
    ([
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 0],
    ], [1, 0, 0, 0], [1, 0, 0, 0]),

    # Third dataset: OR logic
    ([
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 0],
    ], [1, 1, 1, 0], [1, 1, 1, 0]),

    # Fourth dataset: NAND logic
    ([
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 0],
    ], [0, 1, 1, 1], [0, 1, 1, 1]),

])
def test_perceptron_logic(training_data, labels, expected_outputs):
    the_perceptron = Perceptron()
    the_perceptron.train(training_data, labels)

    for i, row in enumerate(training_data):
        assert the_perceptron.predict(row) == expected_outputs[i], f"Expected {expected_outputs[i]} for input {row}"


@pytest.mark.xfail(reason="this test is expected to fail.")
def test_perceptron_failure():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 0],
    ], [1, 1, 1, 0])

    assert the_perceptron.predict([1, 1]) != 1, "Expected failure for input [1,1]"
    assert the_perceptron.predict([1, 0]) == 1, "Expected 1 for input [1,0]"
    assert the_perceptron.predict([0, 1]) == 1, "Expected 1 for input [0,1]"
    assert the_perceptron.predict([0, 0]) == 0, "Expected 0 for input [0,0]"


@pytest.mark.skipif(platform.system() != "Linux" or "ubuntu" not in platform.version().lower(), reason="Test runs only on Linux Ubuntu.")
def test_os_specific_logic():
    # Fetch memory details using os.popen()
    total_memory, used_memory, free_memory = map(
        int, os.popen('free -t -m').readlines()[-1].split()[1:])
    min_memory = 100  # Example: 100MB 
    assert total_memory >= min_memory, f"Expected at least {min_memory/1000} GB of memory. Found only {total_memory/1000} GB."
    min_used_memory = 100  # Example: 100MB
    assert used_memory >= min_used_memory, f"Expected at least {min_used_memory/1000} GB of used memory. Found only {used_memory/1000} GB."
    min_free_memory = 100  # Example: 100MB
    assert free_memory >= min_free_memory, f"Expected at least {min_free_memory/1000} GB of free memory. Found only {free_memory/1000} GB."


@pytest.mark.skip(reason="This test is not yet ready for prime time.")
def test_not_ready():
    print("This won't be printed")
