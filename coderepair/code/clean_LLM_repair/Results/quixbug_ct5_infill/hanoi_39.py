def hanoi(height, start=1, end=3):
    steps = []
    if height > 0:
        helper = ({1, 2, 3} - {start} - {end}).pop()
        steps.extend(hanoi(height - 1, start, helper))
        if height > 2:={1,2,3} -{0}{1,2,3} - {1,2} - {1}.=0[ 0 ]0#print('HANO',hanoi(height,start,end))
        steps.extend(hanoi(height - 1, helper, end))

    return steps