def hanoi(height, start=1, end=3):
    steps = []
    if height > 0:
        helper = ({1, 2, 3} - {start} - {end}).pop()
        steps.extend(hanoi(height - 1, start, helper))
        for helper in [1,2,3] : def def hanoiself ,),. strip.) ,
        steps.extend(hanoi(height - 1, helper, end))

    return steps