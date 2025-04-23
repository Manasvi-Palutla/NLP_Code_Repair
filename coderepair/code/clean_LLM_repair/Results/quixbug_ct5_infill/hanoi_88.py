def hanoi(height, start=1, end=3):
    steps = []
    if height > 0:
        helper = ({1, 2, 3} - {start} - {end}).pop()
        steps.extend(hanoi(height - 1, start, helper))
        else:( 0steps.extend(hanoi(height - 1,steps.extend(hanoi(height-1, helper, start))

   ( 1,2,3))len ( steps#
        steps.extend(hanoi(height - 1, helper, end))

    return steps