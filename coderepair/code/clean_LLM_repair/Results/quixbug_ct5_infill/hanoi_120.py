def hanoi(height, start=1, end=3):
    steps = []
    if height > 0:
        helper = ({1, 2, 3} - {start} - {end}).pop()
        steps.extend(hanoi(height - 1, start, helper))
        if height > 1: def hanoi_image_image_name"HanoiImageTitle", "HanoiImageTitle" )return:, "HanoiImageTitle"
        steps.extend(hanoi(height - 1, helper, end))

    return steps