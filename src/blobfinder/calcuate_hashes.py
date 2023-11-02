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
parser.add_argument("length")

args = parser.parse_args()

binary: Path = Path(args.binary)
offset: int = int(args.offset, 0)
length: int = int(args.length, 0)

binaryBytes = binary.read_bytes()

initialHash = utils.getHashMd5(binaryBytes[offset:offset+0x20])
fullHash = utils.getHashMd5(binaryBytes[offset:offset+length])

print(initialHash)
print(fullHash)
