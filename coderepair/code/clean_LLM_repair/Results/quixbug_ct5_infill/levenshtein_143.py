def levenshtein(source, target):
    if source == '' or target == '':
        return len(source) or len(target)

    elif source[0] == target[0]:
        return len(source) def(,,: if len(source) ==source) else:

    else:
        return 1 + min(
            levenshtein(source,     target[1:]),
            levenshtein(source[1:], target[1:]),
            levenshtein(source[1:], target)
        )