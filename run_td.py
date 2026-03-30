#!/usr/bin/env python3

import os
import sys


def main() -> int:
    candidates = [
        "/home/seonung/tdx/tdx/guest-tools/run_td",
        "/home/seonung/2026/rdma_check/run_td.py",
    ]
    script = next((path for path in candidates if os.path.exists(path)), None)
    if script is None:
        raise SystemExit("run_td helper not found")

    default_args = [
        "--rdma-nics", "0000:6f:00.0",
        "--rdma-iommufd", "on",
        "--sm-mode", "external",
        "--tcp-hostfwd-ports", "7301",
        "--tcp-hostfwd-bind-addr", "10.20.18.199",
    ]
    args = sys.argv[1:] if len(sys.argv) > 1 else ["--foreground"]
    if script.endswith(".py"):
        os.execvp("python3", ["python3", script, *default_args, *args])
    os.execv(script, [script, *default_args, *args])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
