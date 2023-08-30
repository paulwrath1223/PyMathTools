import math


def area_from_minus_one_to_f(f):
    return ((f * (1 - f ** 2) ** 0.5) + math.asin(f)) + math.pi / 2


def semi_circle(p):
    return 2 * (math.sqrt(1 - (p ** 2)))


def get_distances_abs(num_sections, radius):
    target = math.pi / num_sections
    for i in range(num_sections - 1):
        # print(f"solving for cut {i+1}: ")
        answer = numerical_solve(area_from_minus_one_to_f, (target * (i + 1)), semi_circle, 0, 10)
        print(f"cut {i + 1} at {radius + (answer * radius)} units from the side")


def numerical_solve(expression_function, target, ddx_expression_function, initial_guess, iterations):
    current_guess = initial_guess
    for iteration_num in range(iterations):
        last_guess = current_guess
        current_guess = iterate_numerical_solve_get_new_guess(expression_function, target, ddx_expression_function,
                                                              current_guess)
        if math.fabs(current_guess - last_guess) < 0.0000001:
            print(f"numerical solve converged on a value after {iteration_num} iterations")
            break
    return current_guess


def iterate_numerical_solve_get_new_guess(expression_function, target, correction_function, guess):
    delta_y = target - expression_function(guess)
    guess_delta_x = delta_y / correction_function(guess)
    return guess + guess_delta_x


get_distances_abs(5, 10)
