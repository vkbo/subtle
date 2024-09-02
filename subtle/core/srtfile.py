"""
Subtle – SRT File Object
========================

This file is a part of Subtle
Copyright 2024, Veronica Berglyd Olsen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
from __future__ import annotations

import logging

from math import modf
from pathlib import Path

logger = logging.getLogger(__name__)


class SRTReader:

    def __init__(self, path: Path) -> None:
        self._path = path
        self._data: dict[str, tuple[str, str, list[str]]] = {}
        return

    def _readData(self) -> bool:
        """Read SRT info from file."""
        try:
            with open(self._path, mode="r", encoding="utf-8") as fo:
                block = []
                for line in fo:
                    if line:
                        block.append(line)
                    else:
                        self._addBlock(block)
                        block = []
        except Exception as exc:
            logger.error("Could not read SRT file: %s", self._path, exc_info=exc)
            return False
        return True

    def _addBlock(self, block: list[str]) -> None:
        """Add a new frame to internal data."""
        if len(block) > 2:
            num = block[0]
            start, _, end = block[1].partition(" --> ")
            text = block[2:]
            self._data[num] = (start, end, text)
        return


class SRTWriter:

    def __init__(self, path: Path) -> None:
        self._path = path
        self._data: list[tuple[float, float, list[str]]] = []
        return

    def addBlock(self, start: float, end: float, text: list[str]) -> bool:
        """Add a subtitles frame if the timestamps are ok."""
        if start >= 0.0 and end > start:
            self._data.append((start, end, text))
        else:
            logger.warning("Skipping invalid subtitle timestamps start=%.3f end=%.3f", start, end)
            return False
        return True

    def write(self) -> bool:
        """Writer SRT data to file."""
        try:
            with open(self._path, mode="w", encoding="utf-8") as fo:
                prev = -1.0
                for i, (start, end, text) in enumerate(self._data, 1):
                    if start > prev and text:
                        fo.write(f"{i}\n{_formatTS(start)} --> {_formatTS(end)}\n")
                        fo.write("\n".join(text))
                        fo.write("\n\n")
                        prev = start
                    elif start <= prev:
                        logger.warning("Out of order text at t=%s", _formatTS(start))
                    else:
                        logger.warning("Skipping entry with no text at t=%s", _formatTS(start))
        except Exception as exc:
            logger.error("Could not write SRT file: %s", self._path, exc_info=exc)
            return False
        return True


def _formatTS(value: float) -> str:
    """Format float as HH:MM:SS,uuu timestamp."""
    i, f = int(value), round(modf(value)[0]*1000)
    return f"{i//3600:02d}:{i%3600//60:02d}:{i%60:02d},{f:03d}"
