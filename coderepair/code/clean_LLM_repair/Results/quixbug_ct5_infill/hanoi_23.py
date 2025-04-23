def hanoi(height, start=1, end=3):
    steps = []
    if height > 0:
        helper = ({1, 2, 3} - {start} - {end}).pop()
        steps.extend(hanoi(height - 1, start, helper))
        if height > 1: def hanoi (=#print(HANO)=== 2,= 3, start=1,end=3)2,1, end=2,=1,3,end=1). append (1
        steps.extend(hanoi(height - 1, helper, end))

    return steps