from math import exp, log
from Approximation.LinearApproximator import *


class ExponentialApproximator:
    """
    Approximates given data to linear function y = a * e^(b * x).

    Steps:
        1) init
        2) approximate(x_values, y_values)
        3) calculate(x_values)
    """

    def __init__(self):
        self.title = "Exponential"
        self.a = None
        self.b = None

    def approximate(self, x_values, y_values):
        """
        Configures coefficients \'a\' and \'b\' in y = ax + b for object of class.

        Parameters:
            x_values: x values
            y_values: y values for this x values

        Returns:
            True: if data can be approximated linear.
            False: if can't
        """
        for i in range(len(y_values)):
            if y_values[i] <= 0:
                print("Cannot approximate exponentially. (In data y[" + str(i) + "] = " + str(y_values[i]) + ").")
                return False

        log_y = [log(i) for i in y_values]
        linear_approximator = LinearApproximator()
        linear_approximator.approximate(x_values, log_y)
        self.a = linear_approximator.a
        self.b = exp(linear_approximator.b)

        return True

    def function(self, x):
        return self.b * exp(x * self.a)

    def calculate(self, x_values):
        y_values = []
        for i in range(len(x_values)):
            y_values.append(self.function(x_values[i]))
        return y_values
