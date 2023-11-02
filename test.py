#!/usr/bin/env python3

# SPDX-FileCopyrightText: © 2023 Decompollaborate
# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
from pathlib import Path

from src.blobfinder.finder import finder

parser = argparse.ArgumentParser()
parser.add_argument("binary")

args = parser.parse_args()

binary: Path = Path(args.binary)

binaryBytes = binary.read_bytes()

lastEnd = 0

for foundInfo in finder(binaryBytes):
    if lastEnd > 0:
        if lastEnd != foundInfo.start:
            print(f"- [0x{lastEnd:06X}]")
            print()
    print(f"- [0x{foundInfo.start:06X}, {foundInfo.info.sectionToSplat()}, {foundInfo.info.name}]", end="")
    if foundInfo.info.symbols is not None:
        print(f" # symbols: {foundInfo.info.symbols}")
    else:
        print()
    lastEnd = foundInfo.end

if lastEnd > 0:
    print(f"- [0x{lastEnd:06X}]")
