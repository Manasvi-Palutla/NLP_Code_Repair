def hanoi(height, start=1, end=3):
    steps = []
    if height > 0:
        helper = ({1, 2, 3} - {start} - {end}).pop()
        steps.extend(hanoi(height - 1, start, helper))
        for helper in range(1,3):. extend defreturnreturn
        steps.extend(hanoi(height - 1, helper, end))

    return steps