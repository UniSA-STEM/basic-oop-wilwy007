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

def acquire_rig(self, rig: Optional[Rig] = None) -> bool:
    """
    Acquire a rig by consuming a CryptoToken. If rig parameter is None, a default rig is created.
    """
    if self.rig:
        print(f"{self.name}: already has a rig ({self.rig.name}).")
        return False
    if not self._consume_by_name("CryptoToken"):
        print(f"{self.name}: cannot acquire rig — CryptoToken required.")
        return False
    self.rig = rig if rig else Rig(f"{self.name}'s Rig")
    print(f"{self.name}: rig '{self.rig.name}' activated.")
    return True

def upgrade_rig(self) -> bool:
    """Repair the Rig by consuming a CryptoToken"""
    if not self.rig:
        print(f"{self.name}: No Rig to repair).")
        return False
    return self.rig.repair(consumer_callable=self._consume_by_name)

def can_act(self) -> bool:
    """Block actions if trace is above threshold."""
    if self.trace_level > Hacker.trace_threshold:
        print(f"{self.name}: action blocked — trace too high ({self.trace_level}).")
        return False
    return True

def launch_data_spike(self, target_rig: Rig) -> bool:
    """
    Launch a Data Spike at target_rig. Requires a Data Spike in this hacker's rig storage.
    Increases the attacker's trace level by 1.
    """
    if not self.can_act():
        return False
    if self.rig is None:
        print(f"{self.name}: no rig to launch from.")
        return False
    for i, a in enumerate(self.rig.storage):
        if a.name == "Data Spike":
            ds = self.rig.storage.pop(i)
            print(f"{self.name}: launched {ds.name} at {target_rig.name}.")
            target_rig.take_hit()
            self.trace_level += 1
            return True
    print(f"{self.name}: no Data Spike available to launch.")
    return False

def extract_unsecured(self, target_rig: Rig) -> bool:
    """
    Extract all non-encrypted assets from a broken target rig.
    Requires a Removable Drive from hacker inventory or hacker's rig storage.
    """
    if not target_rig.broken:
        print(f"{self.name}: extraction denied — target rig not broken.")
        return False

    drive = self.scan_inventory_for("Removable Drive")
    drive_source = "inventory"
    if drive is None and self.rig:
        for i, a in enumerate(self.rig.storage):
            if a.name == "Removable Drive":
                drive = self.rig.storage.pop(i)
                drive_source = f"{self.rig.name} storage"
                break

    if drive is None:
        print(f"{self.name}: extraction failed — Removable Drive required.")
        return False

    print(f"{self.name}: used Removable Drive from {drive_source} to extract assets.")
    extracted_any = False
    remaining = []
    for a in target_rig.storage:
        if a.encrypted:
            remaining.append(a)
        else:
            self._inventory.append(a)
            print(f"{self.name}: extracted {a.name} from {target_rig.name}.")
            extracted_any = True
    target_rig.storage = remaining
    if not extracted_any:
        print(f"{self.name}: no unsecured assets found.")
    return extracted_any

def encrypt_asset(self, asset_name: str, location: str = "inventory") -> bool:
    """
    Encrypt an asset in inventory or rig storage. Requires a Security Chip in inventory (consumed).
    """
    if not self._consume_by_name("Security Chip"):
        print(f"{self.name}: encryption failed — Security Chip required.")
        return False

    target = None
    if location == "inventory":
        for a in self._inventory:
            if a.name == asset_name:
                target = a
                break
    elif location == "rig" and self.rig:
        for a in self.rig.storage:
            if a.name == asset_name:
                target = a
                break

    if not target:
        print(f"{self.name}: encryption failed — {asset_name} not found in {location}.")
        return False

    target.encrypt()
    print(f"{self.name}: encrypted {target.name} in {location}.")
    return True

def decrypt_asset(self, asset_name: str, location: str = "inventory") -> bool:
    """
    Decrypt an asset in inventory or rig storage. Requires a Security Chip in inventory (consumed).
    """
    if not self._consume_by_name("Security Chip"):
        print(f"{self.name}: decryption failed — Security Chip required.")
        return False

    target = None
    if location == "inventory":
        for a in self._inventory:
            if a.name == asset_name:
                target = a
                break
    elif location == "rig" and self.rig:
        for a in self.rig.storage:
            if a.name == asset_name:
                target = a
                break

    if not target:
        print(f"{self.name}: decryption failed — {asset_name} not found in {location}.")
        return False

    target.decrypt()
    print(f"{self.name}: decrypted {target.name} in {location}.")
    return True