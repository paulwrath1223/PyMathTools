import math

precision = 12  # sets the number of decimal places in the cut positions


def area_from_minus_one_to_f(f):
    """
    :param f: a float representing the positive bound of the integral.
    :return: the area in a circle x^2 + y^2 = 1 between x = -1 and x = f (where ^ is an exponent, not XOR)
    """
    return ((f * (1 - f ** 2) ** 0.5) + math.asin(f)) + math.pi / 2


def semi_circle(p):
    """
    function equal to 'f(x) = 2(sqrt(1-x^2))' (where ^ is an exponent, not XOR)
    this is also the derivative of 'area_from_minus_one_to_f'
    :param p: float, the input of the function (x)
    :return: the value of the above equation at x = p
    """
    return 2 * (math.sqrt(1 - (p ** 2)))


def optimized_get_distances_abs(num_sections, radius):
    """
    print location of cuts that split a circle 'c' into 'n' regions of equal area
    :param num_sections: the number of regions 'n' that the circle 'c' should be split into
    :param radius: the radius of the circle 'c'
    """
    cuts = []
    target = math.pi / num_sections  # the target area of each region.
    for i in range(1, int((num_sections + 1) / 2)):  # for the first half of cuts
        answer = numerical_solve(
            area_from_minus_one_to_f,
            # function that returns the area under a circle from x = -1 to x = f, where f is the function argument
            (target * i),  # the target area between x = -1 and the position of cut i
            semi_circle,  # the derivative of the 'area_from_minus_one_to_f' function
            0,  # a reasonable guess for the position of the cut i. It must be between -1 and 1 inclusive
            10)  # the maximum number of iterations of the 'iterate_numerical_solve_get_new_guess' function
        # because answer is for a circle of radius 1, multiply it by the actual radius to get the real cut position.
        temp_answer = round(answer * radius, precision)
        cuts.append(temp_answer)
    num_cuts = len(cuts)
    if num_sections % 2 == 0:
        cuts.append(0.0)  # if the number of sections is even, there must be a cut in the middle
    for j in range(num_cuts - 1, -1, -1):  # mirror the list of cuts
        cuts.append(-cuts[j])
    return cuts


def numerical_solve(expression_function, target, ddx_expression_function, initial_guess, iterations):
    """
    :param expression_function: the function who's input to optimize towards the value of target
    :param target: the target value of expression function
    :param ddx_expression_function: the derivative of expression_function
    :param initial_guess: a starting guess between -1 and 1
    :param iterations: the number of iterations of the 'iterate_numerical_solve_get_new_guess' function to execute
    :return: the value that passed into 'expression_function' yields target.
    """
    current_guess = initial_guess
    for iteration_num in range(iterations):  # repeat for the number of iterations
        last_guess = current_guess  # update the last answer

        current_guess = iterate_numerical_solve_get_new_guess(  # iterate a new guess
            expression_function,
            target,
            ddx_expression_function,
            current_guess)

        if math.fabs(current_guess - last_guess) < (0.1 ** precision):
            # if the answers are the same up to 'precision' decimal places,
            return current_guess  # then stop iterating because no more precision is needed

    return current_guess  # return the latest guess after all iterations have been executed


def iterate_numerical_solve_get_new_guess(expression_function, target, ddx_expression_function, guess):
    """
    :param expression_function: the function who's input to optimize towards the value of target
    :param target: the target value of expression function
    :param ddx_expression_function: the derivative of expression_function
    :param guess: the correct guess that this function should test
    :return: a new guess that when fed into expression_function yields a value closer to 'target'
    """
    delta_y = target - expression_function(guess)  # measure the difference between f(guess) and the target value
    guess_delta_x = delta_y / ddx_expression_function(guess)
    # if the derivative shows change in y over change in x, then evaluate those values at the guess,
    # and because we know the change in y between our target and the value of f(guess),
    # solve for change in x between guess and the answer.
    # This is not perfect because it assumes the slope is locally linear, which it isn't, so we must continue to iterate
    return guess + guess_delta_x  # apply this change in guess x to the previous guess to get a new value


temp_sections = 4
temp_radius = 7

temp_cuts = optimized_get_distances_abs(temp_sections, temp_radius)

for cut in temp_cuts:
    print(cut)
