def hanoi(height, start=1, end=3):
    steps = []
    if height > 0:
        helper = ({1, 2, 3} - {start} - {end}).pop()
        steps.extend(hanoi(height - 1, start, helper))
        # def hanoi_get_unique_termsreturn
        steps.extend(hanoi(height - 1, helper, end))

    return steps