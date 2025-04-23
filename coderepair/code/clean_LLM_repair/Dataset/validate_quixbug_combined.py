import argparse
import copy
import json
import sys
import types
import shutil
import signal
import os
import glob
import subprocess
from io import StringIO

sys.dont_write_bytecode = True

graph_based = [
    "breadth_first_search", "depth_first_search", "detect_cycle",
    "minimum_spanning_tree", "reverse_linked_list", "shortest_path_length",
    "shortest_path_lengths", "shortest_paths", "topological_ordering"
]

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout

def handler(signum, frame):
    raise Exception("Timeout")

def py_try(algo, *args):
    try:
        if "correct_python_programs." + algo in sys.modules:
            del sys.modules["correct_python_programs." + algo]
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(5)
        module = __import__("correct_python_programs." + algo)
        fx = getattr(module, algo)
        re = getattr(fx, algo)(*args)
        re = prettyprint(re)
        signal.alarm(0)
        return re
    except:
        return sys.exc_info()

def py_try_test(algo):
    try:
        if "correct_python_programs." + algo + "_test" in sys.modules:
            del sys.modules["correct_python_programs." + algo + "_test"]
            del sys.modules["correct_python_programs." + algo]
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(5)
        correct_module = __import__("correct_python_programs." + algo + "_test")
        correct_fx = getattr(correct_module, algo + "_test")
        output = []
        with Capturing(output) as output:
            getattr(correct_fx, "main")()
        signal.alarm(0)
        return ["\n".join(output)]
    except:
        return sys.exc_info()

def prettyprint(o):
    if isinstance(o, types.GeneratorType):
        return "(generator) " + str(list(o))
    else:
        return str(o)

def move_file_and_copy(src, dest, prefix, postfix):
    with open(src, 'r') as f:
        s = f.read()

    # Backup original correct file
    shutil.copy(dest, dest + ".bak")

    # Compose final content to write
    if prefix is not None and postfix is not None:
        final_code = prefix + s + postfix
    else:
        final_code = s

    # Print what is being written
    print("🔧 Writing patched content to:", dest)
    print("-----BEGIN PATCHED CODE-----")
    print(final_code)
    print("------END PATCHED CODE------")

    # Write patched version
    with open(dest, 'w') as f:
        f.write(final_code)


def run_tester(bug, patch_file):
    prefix, postfix = None, None
    with open("QuixBugs/Python/pf.json", 'r') as f:
        data = json.load(f)
        if bug in data:
            prefix = data[bug]["prefix"]
            postfix = data[bug]["postfix"]

    if bug in graph_based:
        correct = py_try_test(bug)
        move_file_and_copy(patch_file, f"QuixBugs/correct_python_programs/{bug}.py", prefix, postfix)
        patch = py_try_test(bug)
        shutil.move(f"QuixBugs/correct_python_programs/{bug}.py.bak", f"QuixBugs/correct_python_programs/{bug}.py")
    else:
        correct = []
        patch = []
        with open(f"QuixBugs/json_testcases/{bug}.json", 'r') as f:
            for line in f:
                py_testcase = json.loads(line)
                test_in, test_out = py_testcase
                if not isinstance(test_in, list):
                    test_in = [test_in]
                c = py_try(bug, *copy.deepcopy(test_in))
                correct.append(c)
                move_file_and_copy(patch_file, f"QuixBugs/correct_python_programs/{bug}.py", prefix, postfix)
                o = py_try(bug, *copy.deepcopy(test_in))
                patch.append(o)
                shutil.move(f"QuixBugs/correct_python_programs/{bug}.py.bak", f"QuixBugs/correct_python_programs/{bug}.py")
                if c != o:
                    return False

    if len(patch) != len(correct):
        return False
    for i, _ in enumerate(patch):
        if patch[i] != correct[i]:
            return False
    return True

def validate_all_patches(folder, j_file):
    with open(os.path.join(folder, j_file), "r") as f:
        repair_dict = json.load(f)

    plausible = 0
    total = 0

    for file in sorted(glob.glob(folder + "/*.py")):
        current_file = "_".join(file.split('/')[-1].split("_")[0:-1])
        if ".py" not in current_file:
            current_file = current_file + ".py"
            try:
                index = int(file.split('/')[-1].split("_")[-1].split(".")[0])
            except:
                current_file = file.split('/')[-1]
                index = 0
        else:
            index = 0

        if len(repair_dict.get(current_file, [])) <= index:
            continue
        if repair_dict[current_file][index]['diff'] == "":
            continue

        bug = current_file.split(".py")[0]
        if run_tester(bug, file):
            plausible += 1
            repair_dict[current_file][index]['valid'] = True
            print(f"{bug} ✓")
        else:
            print(f"{bug} ✗")

        total += 1

    print(f"{plausible}/{total} plausible patches")
    with open(os.path.join(folder, j_file), "w") as f:
        json.dump(repair_dict, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: validate_quixbug.py <results_folder> <lm_repair.json>")
        sys.exit(1)
    validate_all_patches(sys.argv[1], sys.argv[2])
