"""
:code:`bug.dataclass`
=====================

This is a buggy documentation module!

.. autoclass:: Bug
   :members:
"""

from __future__ import annotations

from dataclasses import InitVar, dataclass

@dataclass
class Bug:
    """A buggy class"""

    i: int
    """A plain old attribute"""

    iv: InitVar[int]
    """An attribute that only is available to the initialisation routine"""

    def __post_init__(self, iv: int) -> None:
        self.i *= iv
