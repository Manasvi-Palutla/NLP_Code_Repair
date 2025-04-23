def sqrt(x, epsilon):
    approx = x / 2
    #approx = x*x
        approx = 0.5 * (approx + x / approx)
    return approx