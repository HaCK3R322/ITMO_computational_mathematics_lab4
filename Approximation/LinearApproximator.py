class LinearApproximator:
    """
    Approximates given data to linear function y = ax + b.

    Steps:
        1) init
        2) approximate(x_values, y_values)
        3) calculate(x_values)
    """
    def __init__(self):
        self.title = "Linear"
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
        sx, sxx, sy, sxy = 0, 0, 0, 0
        n = len(x_values)

        for i in range(len(x_values)):
            sx += x_values[i]
            sxx += x_values[i] * x_values[i]
            sy += y_values[i]
            sxy += x_values[i] * y_values[i]

        delta = sxx * n - sx * sx
        delta1 = sxy * n - sx * sy
        delta2 = sxx * sy - sx * sxy

        try:
            self.a = delta1 / delta
            self.b = delta2 / delta
        except ZeroDivisionError:
            print("Cannot do linear approximation.")
            return False
        return True

    def function(self, x):
        return self.a * x + self.b

    def calculate(self, x_values):
        y_values = []
        for i in range(len(x_values)):
            y_values.append(self.function(x_values[i]))
        return y_values
