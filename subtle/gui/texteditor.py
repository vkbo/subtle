"""
Subtle – GUI Text Editor
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

from PyQt6.QtWidgets import QPlainTextEdit, QVBoxLayout, QWidget

logger = logging.getLogger(__name__)


class GuiTextEditor(QWidget):

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.textEdit = QPlainTextEdit(self)

        font = self.textEdit.font()
        font.setPointSizeF(font.pointSizeF() * 3)
        self.textEdit.setFont(font)

        # Assemble
        self.outerBox = QVBoxLayout()
        self.outerBox.addWidget(self.textEdit)

        self.setLayout(self.outerBox)

        return

    def setText(self, text: list[str]) -> None:
        """"""
        self.textEdit.setPlainText("\n".join(text))
        return
