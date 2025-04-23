import subprocess
import json
import glob
import os

def validate_all_patches(folder, j_file):
    with open(os.path.join(folder, j_file), "r") as f:
        repair_dict = json.load(f)

    plausible = 0
    total = 0

    for file in sorted(glob.glob(os.path.join(folder, "*.py"))):
        current_file = "_".join(os.path.basename(file).split("_")[:-1])
        if ".py" not in current_file:
            current_file += ".py"
            try:
                index = int(os.path.basename(file).split("_")[-1].split(".")[0])
            except:
                current_file = os.path.basename(file)
                index = 0
        else:
            index = 0

        print(current_file, index)

        if len(repair_dict[current_file]) <= index:
            print("Error: {}".format(file))
            continue

        print(repair_dict[current_file][index]['diff'])

        if repair_dict[current_file][index]['diff'] == "":
            continue

        bug = current_file.split(".py")[0]

        # Absolute paths for Colab
        python_tester_path = "/content/coderepair/code/clean_LLM_repair/QuixBugs/python_tester.py"
        cmd = f"python {python_tester_path} --bug {bug} --file {file} --add_pf"
        exit_code = subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if exit_code.returncode == 0:
            plausible += 1
            repair_dict[current_file][index]['valid'] = True
            print(f"{bug} has valid patch: {file}")
        else:
            print(f"{bug} has invalid patch: {file}")

        total += 1

    print(f"{plausible}/{total} patches are plausible")

    with open(os.path.join(folder, j_file), "w") as f:
        json.dump(repair_dict, f)
