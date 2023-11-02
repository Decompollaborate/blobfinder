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

finder(binaryBytes)
