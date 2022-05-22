import numpy as np
from numpy.linalg import LinAlgError


class Polynomial2Approximator:
    """
    Approximates given data to polynomial function y = a0 + a1(x) + a2(x^2).

    Steps:
        1) init
        2) approximate(x_values, y_values)
        3) calculate(x_values)
    """
    def __init__(self):
        self.title = "Polynomial2"
        self.a0 = None
        self.a1 = None
        self.a2 = None

    def approximate(self, x_values, y_values):
        """
        Configures coefficients \'a0\', \'a1\', \'a2\' in y = a0 + a1(x) + a2(x^2) for object of class.

        Parameters:
            x_values: x values
            y_values: y values for this x values

        Returns:
            True: if data can be approximated.
            False: if can't.
        """
        sx, sxx, sxxx, sxxxx = 0, 0, 0, 0
        sy, sxy, sxxy = 0, 0, 0
        n = len(x_values)

        for i in range(len(x_values)):
            sx += x_values[i]
            sxx += x_values[i] * x_values[i]
            sxxx += x_values[i] * x_values[i] * x_values[i]
            sxxxx += x_values[i] * x_values[i] * x_values[i] * x_values[i]
            sy += y_values[i]
            sxy += x_values[i] * y_values[i]
            sxxy += x_values[i] * x_values[i] * y_values[i]

        m1 = np.mat([[n, sx, sxx], [sx, sxx, sxxx], [sxx, sxxx, sxxxx]])
        v1 = np.array([sy, sxy, sxxy])

        try:
            answers = np.linalg.solve(m1, v1)
        except LinAlgError:
            print("Cannot approximate polynomial2.")
            return False

        self.a0 = answers[0]
        self.a1 = answers[1]
        self.a2 = answers[2]

        return True

    def function(self, x):
        return self.a0 + self.a1 * x + self.a2 * x * x

    def calculate(self, x_values):
        y_values = []
        for i in range(len(x_values)):
            y_values.append(self.function(x_values[i]))
        return y_values
