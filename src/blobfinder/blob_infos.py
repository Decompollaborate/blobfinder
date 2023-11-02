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
    symbols: str|None = None

    def sectionToSplat(self) -> str:
        if self.sectionType == ".text":
            return "textbin"
        if self.sectionType == ".data":
            return "databin"
        if self.sectionType == ".rodata":
            return "rodatabin"
        if self.sectionType.startswith("."):
            return self.sectionType[1:]
        return self.sectionType


# Key is the hash of the first 0x20 bytes of the blob
blobList: list[BlobInfo] = [
    # IPL3s
    BlobInfo("ipl3_6101",                   0xFC0,      ".data",    "900b4a5b68edb71f4c7ed52acd814fc5", "f226632d4b423607842a2cf5d78553fd"),
    BlobInfo("ipl3_6102_7101",              0xFC0,      ".data",    "e24dd796b2fa16511521139d28c8356b", "24655e01b32541c685f3b86606bf456b"),
    BlobInfo("ipl3_7102",                   0xFC0,      ".data",    "955894c2e40a698bf98a67b78a4e28fa", "24655e01b32541c685f3b86606bf456b"),
    BlobInfo("ipl3_X103",                   0xFC0,      ".data",    "319038097346e12c26c3c21b56f86f23", "24655e01b32541c685f3b86606bf456b"),
    BlobInfo("ipl3_X105",                   0xFC0,      ".data",    "ff22a296e55d34ab0a077dc2ba5f5796", "dcc3971b47b8e9a881319870849d72c6"),
    BlobInfo("ipl3_X106",                   0xFC0,      ".data",    "6460387749ac0bd925aa5430bc7864fe", "24655e01b32541c685f3b86606bf456b"),

    # RSP ucodes
    BlobInfo("rspboot",                     0xD0,       ".text",    "9414dd746eddee59ce6bf97eca16853e", "3fcedf9860921eb8c4f8a3be67de308d", "rspbootTextStart/rspbootTextEnd"),
    BlobInfo("aspMain",                     0xE20,      ".text",    "ee3aec6ffbe9880deb32e8f00bc47cf1", "b8376970c6e6edb55c71a351750384b5", "aspMainTextStart/aspMainTextEnd"),
    BlobInfo("aspMain",                     0x2C0,      ".data",    "78147a7b28db17f7e6fbf53c38bf2082", "aacf4a320e9a29eddf5bd82be64e0e88", "aspMainDataStart/aspMainDataEnd"),
    BlobInfo("f3dex2",                      0x1390,     ".text",    "6ccf5fc392e440fb23bc7d7f7d71047c", "09bb03ca1eff937be2cf04c78c5ccd4a", "gspF3DEX2_fifoTextStart/gspF3DEX2_fifoTextEnd"),
    BlobInfo("f3dex2",                      0x420,      ".data",    "3a3a406acb4295d33fa6e918dd3a7ae4", "70bc8f4b72a86921468bf8e8441dce51", "gspF3DEX2_fifoDataStart/gspF3DEX2_fifoDataEnd"),
    BlobInfo("s2dex",                       0x17F0,     ".text",    "e45f2fc60e5a542d3609bf0f1ae3ed6c", "bda84c8593e8a296ae0cdcc582218bfa", "gspS2DEX_fifoTextStart/gspS2DEX_fifoTextEnd"),
    BlobInfo("s2dex",                       0x3C0,      ".data",    "382e3a4f39410248b142d98bbe0a54a5", "70bc8f4b72a86921468bf8e8441dce51", "gspS2DEX_fifoDataStart/gspS2DEX_fifoDataEnd"),

]

initialHashesDict: dict[str, list[BlobInfo]] = dict()
for x in blobList:
    if x.initialHashStr not in initialHashesDict:
        initialHashesDict[x.initialHashStr] = []
    initialHashesDict[x.initialHashStr].append(x)
