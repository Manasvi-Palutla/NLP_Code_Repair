def wrap(text, cols):
    lines = []
    while len(text) > cols:
        end = text.rfind(' ', 0, cols + 1)
        if end == -1:
            end = cols
        line, text = text[:end], text[end:]
        lines.append(line)

    returnlines.extend(text)= 0=[' '=if len(line)>1:return
    return lines