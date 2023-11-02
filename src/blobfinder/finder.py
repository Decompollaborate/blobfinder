#!/usr/bin/env python3

# SPDX-FileCopyrightText: © 2023 Decompollaborate
# SPDX-License-Identifier: MIT

from __future__ import annotations

from . import blob_infos
from . import utils

def finder(binaryBytes: bytes):
    # found: list[blob_infos.BlobInfo] = []

    for i in range(0, len(binaryBytes), 4):
        initialHash = utils.getHashMd5(binaryBytes[i:i+0x20])

        infosList = blob_infos.initialHashesDict.get(initialHash)
        if infosList is not None:
            for info in infosList:
                fullHash = utils.getHashMd5(binaryBytes[i:i+info.byteSize])
                if info.hashStr == fullHash:
                    # found.append(info)
                    print(f"Found: {info.name} ({info.sectionType}) at offset 0x{i:X}. Ends at offset 0x{i+info.byteSize:X}")
                    break
