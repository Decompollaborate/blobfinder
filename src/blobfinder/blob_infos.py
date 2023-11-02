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
    initialHashStr: str # hash of the first 0x20 bytes
    symbols: str|None = None
    variant: str|None = None

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


blobList: list[BlobInfo] = [
    # IPL3s
    BlobInfo("ipl3_6101",                       0xFC0,      ".data",    "900b4a5b68edb71f4c7ed52acd814fc5", "f226632d4b423607842a2cf5d78553fd"),
    BlobInfo("ipl3_6102_7101",                  0xFC0,      ".data",    "e24dd796b2fa16511521139d28c8356b", "24655e01b32541c685f3b86606bf456b"),
    BlobInfo("ipl3_7102",                       0xFC0,      ".data",    "955894c2e40a698bf98a67b78a4e28fa", "24655e01b32541c685f3b86606bf456b"),
    BlobInfo("ipl3_X103",                       0xFC0,      ".data",    "319038097346e12c26c3c21b56f86f23", "24655e01b32541c685f3b86606bf456b"),
    BlobInfo("ipl3_X105",                       0xFC0,      ".data",    "ff22a296e55d34ab0a077dc2ba5f5796", "dcc3971b47b8e9a881319870849d72c6"),
    BlobInfo("ipl3_X106",                       0xFC0,      ".data",    "6460387749ac0bd925aa5430bc7864fe", "24655e01b32541c685f3b86606bf456b"),

    # libultra RSP ucodes
    BlobInfo("rspboot",                         0xD0,       ".text",    "9414dd746eddee59ce6bf97eca16853e", "3fcedf9860921eb8c4f8a3be67de308d", "rspbootTextStart/rspbootTextEnd", variant=None),
    BlobInfo("rspboot",                         0x160,      ".text",    "71a783d5a6bd3eb289cad5ecd1c3f71d", "8375a7f115d082ffcb2b7fd69b7873e6", "rspbootTextStart/rspbootTextEnd", variant="zelda64"),

    BlobInfo("aspMain",                         0xE20,      ".text",    "ee3aec6ffbe9880deb32e8f00bc47cf1", "b8376970c6e6edb55c71a351750384b5", "aspMainTextStart/aspMainTextEnd", variant=None),
    BlobInfo("aspMain",                         0x2C0,      ".data",    "78147a7b28db17f7e6fbf53c38bf2082", "aacf4a320e9a29eddf5bd82be64e0e88", "aspMainDataStart/aspMainDataEnd", variant=None),

    # TODO: identify variants
    BlobInfo("s2dex",                           0x17F0,     ".text",    "e45f2fc60e5a542d3609bf0f1ae3ed6c", "bda84c8593e8a296ae0cdcc582218bfa", "gspS2DEX_fifoTextStart/gspS2DEX_fifoTextEnd"),
    BlobInfo("s2dex",                           0x3C0,      ".data",    "382e3a4f39410248b142d98bbe0a54a5", "70bc8f4b72a86921468bf8e8441dce51", "gspS2DEX_fifoDataStart/gspS2DEX_fifoDataEnd"),
    BlobInfo("f3dex",                           0x1430,     ".text",    "6b329f3fdf0fb041e27acd3b285365c8", "821377b6549d6678b4ff4788261206b4", "gspF3DEX_fifoTextStart/gspF3DEX_fifoTextEnd"),
    BlobInfo("f3dex",                           0x800,      ".data",    "d325f5320c218baa2d498e6534aeae70", "71b88f48ae185fcad29a58887adb936f", "gspF3DEX_fifoDataStart/gspF3DEX_fifoDataEnd"),
    BlobInfo("f3dex2",                          0x1390,     ".text",    "6ccf5fc392e440fb23bc7d7f7d71047c", "09bb03ca1eff937be2cf04c78c5ccd4a", "gspF3DEX2_fifoTextStart/gspF3DEX2_fifoTextEnd"),
    BlobInfo("f3dex2",                          0x420,      ".data",    "3a3a406acb4295d33fa6e918dd3a7ae4", "70bc8f4b72a86921468bf8e8441dce51", "gspF3DEX2_fifoDataStart/gspF3DEX2_fifoDataEnd"),
    BlobInfo("gspS2DEX2.fifo",                  0x18C0,     ".text",    "cb9d0bbc102e8a0ac03924ec08822cb6", "3ace7bd6f0cd931185f85155cabd6ccf", "gspS2DEX2_fifoTextStart/gspS2DEX2_fifoTextEnd"),
    BlobInfo("gspS2DEX2.fifo",                  0x390,      ".data",    "e62b84a39e6bc4cfd63d9e7751217743", "70bc8f4b72a86921468bf8e8441dce51", "gspS2DEX2_fifoDataStart/gspS2DEX2_fifoDataEnd"),
    BlobInfo("gspF3DZEX2.NoN.PosLight.fifo",    0x1630,     ".text",    "ca0a31df36dbeda69f09e9850e68c7f7", "c705d6568ec32358d0efbfc452838304", "gspF3DZEX2_NoN_PosLight_fifoTextStart/gspF3DZEX2_NoN_PosLight_fifoTextEnd"),
    BlobInfo("gspF3DZEX2.NoN.PosLight.fifo",    0x420,      ".data",    "d31cea0e173c6a4a09e4dfe8f259c91b", "70bc8f4b72a86921468bf8e8441dce51", "gspF3DZEX2_NoN_PosLight_fifoDataStart/gspF3DZEX2_NoN_PosLight_fifoDataEnd"),
    BlobInfo("njpgdspMain",                     0xAF0,      ".text",    "1cab4dc7403c218956adc82dffc624c0", "5dbbfd793057ddf9ae019deb79892a2b", "njpgdspMainTextStart/njpgdspMainTextEnd"),
    BlobInfo("njpgdspMain",                     0x60,       ".data",    "cf5303b2528507dad6da93df2a52a01f", "a02bb989958a678f5cb61bd8ac2b06d4", "njpgdspMainDataStart/njpgdspMainDataEnd"),

    # HVQM2
    BlobInfo("hvqm2sp1",                        0x5D0,      ".text",    "1fb32836fe499c4ef6ab5ca6fc0fed52", "a1e49982be78f96fab5d7615fb1fe734", "hvqm2sp1DataStart/hvqm2sp1DataEnd"),
    BlobInfo("hvqm2sp1",                        0xD50,      ".data",    "e2f6443aa7d009d9b35ff48f934a2151", "f653e178ed1acfe1cf2564141a64b3ae", "hvqm2sp1DataStart/hvqm2sp1DataEnd"),
    # TODO: hvqm2sp2
    # BlobInfo("hvqm2sp2",                     ,       ".text",    "", "", ""),
    # BlobInfo("hvqm2sp2",                     ,       ".data",    "", "", ""),

]

initialHashesDict: dict[str, list[BlobInfo]] = dict()
for x in blobList:
    if x.initialHashStr not in initialHashesDict:
        initialHashesDict[x.initialHashStr] = []
    initialHashesDict[x.initialHashStr].append(x)
