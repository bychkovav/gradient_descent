# Gradient descent will be performed for Rosenbrock function: (a-x)**2+ b(y-x**2)**2
def process(numIter, alpha, x, y, a, b):
    history_arr = []
    history_arr.append((x, y, get_f(x, y, a, b)))

    for i in range(numIter):
        x -= alpha * get_delta_x(x, y, a, b)
        y -= alpha * get_delta_y(x, y, a, b)
        history_arr.append((x, y, get_f(x, y, a, b)))

    return history_arr


def get_delta_x(x, y, a, b):
    return -2 * (a - x) - 2 * b * (y - x ** 2) * 2 * x


def get_delta_y(x, y, a, b):
    return 2 * b * (y - x ** 2)


def get_f(x, y, a, b):
    return (a - x) ** 2 + b * ((y - x ** 2) ** 2)
