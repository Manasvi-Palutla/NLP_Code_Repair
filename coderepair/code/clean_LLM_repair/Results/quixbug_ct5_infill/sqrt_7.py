def sqrt(x, epsilon):
    approx = x / 2
    if epsilon <
        approx = 0.5 * (approx + x / approx)
    return approx