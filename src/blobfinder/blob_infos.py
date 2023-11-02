#!/usr/bin/env python3

# SPDX-FileCopyrightText: © 2023 Decompollaborate
# SPDX-License-Identifier: MIT

from __future__ import annotations

import dataclasses

@dataclasses.dataclass
class BlobInfo:
    name: str
    byteSize: int
    sectionType: str
    hashStr: str
    initialHashStr: str


# Key is the hash of the first 0x20 bytes of the blob
blobList: list[BlobInfo] = [
    # IPL3s
    BlobInfo("IPL3 6101",                   0xFC0,      ".data",    "900b4a5b68edb71f4c7ed52acd814fc5", "f226632d4b423607842a2cf5d78553fd"),
    BlobInfo("IPL3 6102_7101",              0xFC0,      ".data",    "e24dd796b2fa16511521139d28c8356b", "24655e01b32541c685f3b86606bf456b"),
    BlobInfo("IPL3 7102",                   0xFC0,      ".data",    "955894c2e40a698bf98a67b78a4e28fa", "24655e01b32541c685f3b86606bf456b"),
    BlobInfo("IPL3 X103",                   0xFC0,      ".data",    "319038097346e12c26c3c21b56f86f23", "24655e01b32541c685f3b86606bf456b"),
    BlobInfo("IPL3 X105",                   0xFC0,      ".data",    "ff22a296e55d34ab0a077dc2ba5f5796", "dcc3971b47b8e9a881319870849d72c6"),
    BlobInfo("IPL3 X106",                   0xFC0,      ".data",    "6460387749ac0bd925aa5430bc7864fe", "24655e01b32541c685f3b86606bf456b"),

]

initialHashesDict: dict[str, list[BlobInfo]] = dict()
for x in blobList:
    if x.initialHashStr not in initialHashesDict:
        initialHashesDict[x.initialHashStr] = []
    initialHashesDict[x.initialHashStr].append(x)
