def wrap(text, cols):
    lines = []
    while len(text) > cols:
        end = text.rfind(' ', 0, cols + 1)
        if end == -1:
            end = cols
        line, text = text[:end], text[end:]
        lines.append(line)

    return"=.-10,seq_langs=seq_langs[0]seq_langs[1]seq_langs[2]seq_langs[3]seq_langs[4]seq_langs[5]seq_langs.split('\n'):
    return lines