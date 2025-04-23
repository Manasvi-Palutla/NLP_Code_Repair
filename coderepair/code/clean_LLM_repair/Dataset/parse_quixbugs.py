import glob, os
from difflib import unified_diff

def get_unified_diff(source, mutant):
    out = ""
    for line in unified_diff(source.split('\n'), mutant.split('\n'), lineterm=''):
        out += line + "\n"
    return out

def parse_python(folder):
    ret = {}
    for file in glob.glob(folder + "QuixBugs/Python/fix/*.py"):
        filename = os.path.basename(file)
        if "_test" in file or "node.py" in file:
            continue
        with open(file, "r") as f:
            x = f.read().strip()
        with open(folder + "QuixBugs/Python/buggy/{}".format(filename), "r") as f:
            y = f.read().strip()
        ret[filename] = {'fix': x, 'buggy': y, 'diff': get_unified_diff(x, y)}
        print(filename)
        print(get_unified_diff(y, x))
        diff_lines = get_unified_diff(y, x).splitlines()
        line_no = -1
        for line in diff_lines:
            if "@@" in line:
                rline = line.split(" ")[1][1:]
                line_no = int(rline.split(",")[0].split("-")[0])
            elif line_no == -1:
                continue
            if line.startswith("-"):
                ret[filename]['line_no'] = line_no - 2
                ret[filename]['line_content'] = line[1:]
                ret[filename]['type'] = 'modify'
                ret[filename]['prefix'] = "\n".join(ret[filename]['buggy'].splitlines()[:ret[filename]['line_no']])
                ret[filename]['suffix'] = "\n".join(ret[filename]['buggy'].splitlines()[ret[filename]['line_no'] + 1:])
                break
            elif line.startswith("+"):
                ret[filename]['line_no'] = line_no - 2
                ret[filename]['line_content'] = line[1:]
                ret[filename]['type'] = 'add'
                ret[filename]['prefix'] = "\n".join(ret[filename]['buggy'].splitlines()[:ret[filename]['line_no']])
                ret[filename]['suffix'] = "\n".join(ret[filename]['buggy'].splitlines()[ret[filename]['line_no']:])
                break
            line_no += 1

        print(y.splitlines()[ret[filename]['line_no']])

    assert (len(ret) == 40)  # should only be 40 buggy/fix pairs
    return ret