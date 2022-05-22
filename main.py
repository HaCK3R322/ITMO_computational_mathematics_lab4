import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from read_from_file import read


from Approximation.LinearApproximator import *
from Approximation.Polynomial2Approximator import *
from Approximation.Polynomial3Approximator import *
from Approximation.ExponentialApproximator import *
from Approximation.LogarithmicApproximator import *
from Approximation.PowerApproximator import *


def function_var1(x):
    return (2 * x) / (x * x * x * x + 1)


def calculate_y(x_values, function):
    y_values = []
    for i in range(len(x_values)):
        y_values.append(function(x_values[i]))
    return y_values


def do_all_the_stuff(x_values, y_values, approximator, title):
    more_x_values = np.linspace(x_values[0], x_values[len(x_values) - 1], len(x_values) * 10)  # get more x values
    if approximator.approximate(x_values, y_values):  # approximate
        approximated_y_vals = approximator.calculate(x_values)
        more_approximated_y_vals = approximator.calculate(more_x_values)  # to print
        standard_deviation = round(calculate_standard_deviation(x_values, y_values, approximated_y_vals), 3)

        print(title + " standard deviation = " + str(standard_deviation))
        plt.title(title + " (Standard deviation = " + str(standard_deviation) + ")")
        plt.plot(xarr, yarr, 'bo')
        plt.plot(more_x_values, more_approximated_y_vals, "r")
        plt.show()


def calculate_standard_deviation(x_values, y_values, new_y_values):
    summary = 0
    for i in range(len(x_values)):
        summary += (y_values[i] - new_y_values[i]) ** 2
    summary /= len(x_values)
    return sqrt(summary)


def find_best_approximator(x_values, y_values, *approximators):  # we already configured all approximation coefficients
    min_sd = 0
    min_name = ''
    for first in approximators:
        try:
            approximated_y_vals = first.calculate(x_values)
            min_sd = round(calculate_standard_deviation(x_values, y_values, approximated_y_vals), 3)
            min_name = first.title
            break
        except (TypeError, ValueError):
            continue

    for approximator in approximators:
        try:
            approximated_y_vals = approximator.calculate(x_values)
            standard_deviation = round(calculate_standard_deviation(x_values, y_values, approximated_y_vals), 3)
            if min_sd > standard_deviation:
                min_sd = standard_deviation
                min_name = approximator.title
        except (ValueError, TypeError):
            continue

    print("\nBest approximation:", min_name, "    Standard deviation =", min_sd)


if __name__ == '__main__':
    plt.close("all")

    a = 0
    b = 2
    h = 0.2
    number_of_points = int((b - a) / h) + 1

    xarr = np.linspace(a, b, number_of_points)
    yarr = calculate_y(xarr, function_var1)

    answer = input("Dou ypu wanna get data from file? (y/anything)\n")
    if answer == "y":
        file_path = input("Enter file path:\n>>> ")
        try:
            data = read(file_path)
            xarr = data['xarr']
            yarr = data['yarr']
        except FileNotFoundError:
            print("No such file. Initializing standard algorithm:\n")

    linear = LinearApproximator()
    pol2 = Polynomial2Approximator()
    pol3 = Polynomial3Approximator()
    exponential = ExponentialApproximator()
    logarithmic = LogarithmicApproximator()
    power = PowerApproximator()

    do_all_the_stuff(xarr, yarr, linear, "Linear approximation")
    do_all_the_stuff(xarr, yarr, pol2, "Pol2 approximation")
    do_all_the_stuff(xarr, yarr, pol3, "Pol3 approximation")
    do_all_the_stuff(xarr, yarr, exponential, "Exp approximation")
    do_all_the_stuff(xarr, yarr, logarithmic, "Log approximation")
    do_all_the_stuff(xarr, yarr, power, "Pow approximation")

    find_best_approximator(xarr, yarr, linear, pol2, pol3, exponential, logarithmic, power)
