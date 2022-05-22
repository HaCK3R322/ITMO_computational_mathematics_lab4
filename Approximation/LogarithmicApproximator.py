from math import log
from Approximation.LinearApproximator import *


class LogarithmicApproximator:
    """
    Approximates given data to logarithmic function y = a*ln(x) + b.

    Steps:
        1) init
        2) approximate(x_values, y_values)
        3) calculate(x_values)
    """

    def __init__(self):
        self.title = "Logarithmic"
        self.a = None
        self.b = None

    def approximate(self, x_values, y_values):
        """
        Configures coefficients \'a\' and \'b\' in y = ax + b for object of class.

        Parameters:
            x_values: x values
            y_values: y values for this x values

        Returns:
            True: if data can be approximated logarithmically.
            False: if can't
        """
        for i in range(len(x_values)):
            if x_values[i] <= 0:
                print("Cannot approximate logarithmically. (In data x[" + str(i) + "] = " + str(x_values[i]) + ").")
                return False

        log_x = [log(i) for i in x_values]
        linear_approximator = LinearApproximator()
        linear_approximator.approximate(log_x, y_values)
        self.a = linear_approximator.a
        self.b = linear_approximator.b

        return True

    def function(self, x):
        return self.a * log(x) + self.b

    def calculate(self, x_values):
        y_values = []
        for i in range(len(x_values)):
            y_values.append(self.function(x_values[i]))
        return y_values
