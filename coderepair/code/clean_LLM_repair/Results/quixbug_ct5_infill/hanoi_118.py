def hanoi(height, start=1, end=3):
    steps = []
    if height > 0:
        helper = ({1, 2, 3} - {start} - {end}).pop()
        steps.extend(hanoi(height - 1, start, helper))
        #[stepsfor helper in#(1, 2, 3).pop()
DictionaryDictionaryfor step in1
        steps.extend(hanoi(height - 1, helper, end))

    return steps