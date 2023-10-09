"""Module docstring: Briefly describe the module here."""

class Perceptron:
    """Class docstring: Briefly describe the class."""

    def __init__(self):
        """Function docstring: function description"""
        self._weights = []

    def train(self, inputs, labels):
        """Function docstring: briefly describe the function."""
        dummied_inputs = [data + [-1] for data in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])
        for _ in range(5000):
            for input_data, label in zip(dummied_inputs, labels):
                label_delta = label - self.predict(input_data)
                for index, value in enumerate(input_data):
                    self._weights[index] += 0.1 * value * label_delta

    def predict(self, input_data):
        """Function docstring: briefly describe function."""
        if len(input_data) == 0:
            return None
        input_data = input_data + [-1]
        return int(0 < sum(value[0] * value[1] for value in zip(self._weights, input_data)))
