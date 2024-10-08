"""
Subtle – OCR Base Class
=======================

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

from abc import ABC, abstractmethod

from PyQt6.QtGui import QImage

logger = logging.getLogger(__name__)


class OCRBase(ABC):

    def __init__(self) -> None:
        return

    @abstractmethod
    def processImage(self, index: int, image: QImage, lang: list[str]) -> list[str]:
        raise NotImplementedError
