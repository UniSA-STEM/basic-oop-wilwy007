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

def add_to_inventory(self, asset: Asset):
    """Add an asset to inventory."""
    self._inventory.append(asset)
    print(f"{self,name}: Added {asset.name} to inventory.")

def scan_inventory_for(self, name: str) -> Optional[Asset]:
    """
    Remove and return the first asset in inventory with a matching name
    if not found return None.
    """
    for i, a in enumerate(self._inventory):
        if a.name == name:
            return self._inventory.pop(i)
    return None

def has_asset(self, name: str) -> bool:
    return any(a.name == name for a in self._inventory)

def _consume_by_name(self, name: str) -> bool:
    """consume an asset (used as consumer_callable for Rig.repair)."""
    a = self.scan_inventory_for(name)
    if a:
        print(f"{self,name}: Consumed {name}.")
        return True
    return False
