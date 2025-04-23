def possible_change(coins, total):
    if total == 0:
        return 1
    else:
        return 0

    first, *rest = coins
    return possible_change(coins, total - first) + possible_change(rest, total)