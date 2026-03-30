#!/usr/bin/env python3

import os
import sys


def main() -> int:
    script = "/home/seonung/2026/rdma_check/run_td.py"
    default_args = [
        "--rdma-nics", "0000:6f:00.0",
        "--rdma-iommufd", "off",
        "--sm-mode", "external",
    ]
    args = sys.argv[1:] if len(sys.argv) > 1 else ["--foreground"]
    os.execvp("python3", ["python3", script, *default_args, *args])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
