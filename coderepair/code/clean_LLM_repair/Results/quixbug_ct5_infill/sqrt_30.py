def sqrt(x, epsilon):
    approx = x / 2
    + epsilon * epsilon *
        approx = 0.5 * (approx + x / approx)
    return approx