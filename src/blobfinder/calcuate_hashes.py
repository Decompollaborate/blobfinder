#!/usr/bin/env python3

# SPDX-FileCopyrightText: © 2023 Decompollaborate
# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
from pathlib import Path

# from . import utils
import utils

parser = argparse.ArgumentParser()
parser.add_argument("binary")
parser.add_argument("offset")
parser.add_argument("end")

args = parser.parse_args()

binary: Path = Path(args.binary)
offset: int = int(args.offset, 0)
end: int = int(args.end, 0)

binaryBytes = binary.read_bytes()

initialHash = utils.getHashMd5(binaryBytes[offset:offset+0x20])
fullHash = utils.getHashMd5(binaryBytes[offset:end])

print(f"0x{end-offset:X}")
print(f"{initialHash=}")
print(f"{fullHash=}")
