from math import log, exp
from Approximation.LinearApproximator import *


class PowerApproximator:
    """
    Approximates given data to power function y = a * x^b.

    Steps:
        1) init
        2) approximate(x_values, y_values)
        3) calculate(x_values)
    """

    def __init__(self):
        self.title = "Power"
        self.a = None
        self.b = None

    def approximate(self, x_values, y_values):
        """
        Configures coefficients \'a\' and \'b\' in y = a * x^b for object of class.

        Parameters:
            x_values: x values
            y_values: y values for this x values

        Returns:
            True: if data can be approximated logarithmically.
            False: if can't
        """
        for i in range(len(x_values)):
            if x_values[i] <= 0:
                print("Cannot approximate by pow. (In data x[" + str(i) + "] = " + str(x_values[i]) + ").")
                return False
            if y_values[i] <= 0:
                print("Cannot approximate by pow. (In data y[" + str(i) + "] = " + str(y_values[i]) + ").")
                return False

        log_x = [log(i) for i in x_values]
        log_y = [log(i) for i in y_values]
        linear_approximator = LinearApproximator()
        linear_approximator.approximate(log_x, log_y)
        self.a = exp(linear_approximator.b)
        self.b = linear_approximator.a

        return True

    def function(self, x):
        return self.a * (x ** self.b)

    def calculate(self, x_values):
        y_values = []
        for i in range(len(x_values)):
            y_values.append(self.function(x_values[i]))
        return y_values
