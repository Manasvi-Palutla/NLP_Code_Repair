INFILL_START = "<extra_id_0>"
INFILL_END   = "<extra_id_1>"

def build_infill_prompt(prefix: str, suffix: str) -> str:
    if not prefix.endswith("\n"): prefix += "\n"
    if not suffix.startswith("\n"): suffix = "\n" + suffix
    return prefix + INFILL_START + "\n" + INFILL_END + suffix

