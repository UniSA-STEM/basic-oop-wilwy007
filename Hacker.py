"""
File: Hacker.py
Description: The Hacker class represents hacker character. It manages
    inventory and rig and actions like attacks, encryption, upgrading and trace
    management.
Author: William Willoughby
ID: 110477792
Username: wilwy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from typing import List, Optional
from Asset import Asset
from Rig import Rig

class Hacker:
    trace_threshold = 5

    def __init__(self, name: str):
        self.name = name
        self._inventory: List[Asset] = [Asset("CryptoToken", "Starter Token")]
        self._rig: Optional[Rig] = None
        self.trace_level = 0

    def __str__(self) -> str:
        inv = ", ".join([str(a) for a in self._inventory]) or "Empty"
        rig_name = self.rig.name if self.rig else "No Rig"
        return f"Hacker: {self.name} | Rig: {rig_name} | Trace: {self.trace_level} | Inventory: [{inv}]"
