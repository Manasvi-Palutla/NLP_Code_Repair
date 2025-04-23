def sqrt(x, epsilon):
    approx = x / 2
    if epsilon > 1e-10 :
        approx = 0.5 * (approx + x / approx)
    return approx