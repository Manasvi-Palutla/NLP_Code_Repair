def hanoi(height, start=1, end=3):
    steps = []
    if height > 0:
        helper = ({1, 2, 3} - {start} - {end}).pop()
        steps.extend(hanoi(height - 1, start, helper))
        while height > 0:.(-:- 1, end)#2, 3, 4, 5
        steps.extend(hanoi(height - 1, helper, end))

    return steps