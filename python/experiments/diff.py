#  Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
#  Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.

from itertools import chain
from pathlib import Path
from subprocess import run
from typing import Optional

copied_dirs = [
    ("../../compiler/ir/backend.js/src", "../../compiler/ir/backend.py/src"),
    ("../../compiler/cli/cli-js/src", "../../compiler/cli/cli-py/src"),
    ("../../js/js.inliner/src", "../../python/py.inliner/src"),
    ("../../js/js.translator/src", "../../python/py.translator/src"),
]


def compare(path1: str, path2: str) -> str:
    cmd = ["git", "--no-pager", "diff", "--no-index", "--unified=0"]
    run_result = run(cmd + [path1, path2], capture_output=True)
    return run_result.stdout.decode("utf-8")


def is_interesting_line(line: str) -> bool:
    return (not line.startswith("@@")) and \
           (not line.startswith("- *")) and (not line.startswith("+ *")) and \
           (not line.startswith("-package")) and (not line.startswith("+package")) and \
           (not line.startswith("-import")) and (not line.startswith("+import"))


def find_interesting_diff_or_none(diff: str) -> Optional[str]:
    diff_lines = diff.splitlines()[4:]
    interesting_lines = list(filter(is_interesting_line, diff_lines))
    if len(interesting_lines) == 0:
        return None
    else:
        return "\n".join(interesting_lines)


skip_not_interesting = True
skipped = 0
found = 0
total = 0

for (src, dst) in copied_dirs:
    for dst_path in chain(Path(dst).glob("**/*.kt"), Path(dst).glob("**/*.java")):
        total += 1
        src_path = Path(str(dst_path).replace(dst, src).replace("py", "js"))
        if src_path.exists():
            diff = find_interesting_diff_or_none(compare(str(src_path.absolute()), str(dst_path.absolute())))
            found += 1
            if diff is None and skip_not_interesting:
                skipped += 1
                continue

            print("vvv", dst_path, "vvv")
            if diff is not None:
                print(diff)

print("skipped:", skipped)
print("found:", found)
print("total:", total)
