#!/usr/bin/env python3

# SPDX-FileCopyrightText: © 2023 Decompollaborate
# SPDX-License-Identifier: MIT

from __future__ import annotations

import dataclasses
from typing import Iterable

from . import blob_infos
from . import utils

@dataclasses.dataclass
class FoundInfo:
    start: int
    end: int
    info: blob_infos.BlobInfo

def finder(binaryBytes: bytes) -> Iterable[FoundInfo]:
    for i in range(0, len(binaryBytes), 4):
        initialHash = utils.getHashMd5(binaryBytes[i:i+0x20])

        infosList = blob_infos.initialHashesDict.get(initialHash)
        if infosList is not None:
            for info in infosList:
                fullHash = utils.getHashMd5(binaryBytes[i:i+info.byteSize])
                if info.hashStr == fullHash:
                    yield FoundInfo(i, i+info.byteSize, info)
                    break
