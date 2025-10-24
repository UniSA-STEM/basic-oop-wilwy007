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

    @property
    def rig(self) -> Optional[Rig]:
        """Return the hacker's rig (or None if no rig)."""
        return self._rig

    @rig.setter
    def rig(self, value: Rig):
        """Set the hacker's rig."""
        self._rig = value

    def __str__(self) -> str:
        inv = ", ".join([str(a) for a in self._inventory]) or "Empty"
        rig_name = self.rig.name if self.rig else "No Rig"
        return f"Hacker: {self.name} | Rig: {rig_name} | Trace: {self.trace_level} | Inventory: [{inv}]"

    def add_to_inventory(self, asset: Asset):
        """Add an asset to inventory."""
        self._inventory.append(asset)
        print(f"{self.name}: Added {asset.name} to inventory.")

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
            print(f"{self.name}: Consumed {name}.")
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
        print(f"{self.name}: Rig '{self.rig.name}' activated.")
        return True

    def repair_rig(self) -> bool:
        """Repair the Rig by consuming a CryptoToken"""
        if not self.rig:
            print(f"{self.name}: No Rig to repair.")
            return False
        return self.rig.repair(consumer_callable=self._consume_by_name)

    def upgrade_rig(self) -> bool:
        """Upgrade the Hacker's rig by consuming a Hardware Patch."""
        if not self.rig:
            print(f"{self.name}: No Rig to upgrade.")
            return False
        if not self._consume_by_name("Hardware Patch"):
            print(f"{self.name}: Cannot upgrade — Hardware Patch required.")
            return False
        self.rig.upgrade()
        return True

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
            print(f"{self.name}: Encryption failed — Security Chip required.")
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

    def store_to_rig(self, asset_name: str) -> bool:
        """Move an item from hacker inventory to rig storage (if rig exists)."""
        if not self.rig:
            print(f"{self.name}: no rig to store into.")
            return False
        for i, a in enumerate(self._inventory):
            if a.name == asset_name:
                if self.rig.store_asset(a):
                    self._inventory.pop(i)
                    self.trace_level += 1
                    print(f"{self.name}: stored {asset_name} into {self.rig.name}.")
                    return True
                else:
                    return False
        print(f"{self.name}: no asset named '{asset_name}' in inventory.")
        return False

    def retrieve_from_rig(self, asset_name: str) -> bool:
        """Get an asset from own rig storage and put it into inventory (refuses encrypted assets)."""
        if not self.rig:
            print(f"{self.name}: no rig to retrieve from.")
            return False
        asset = self.rig.release_asset(asset_name)
        if asset is None:
            return False
        self._inventory.append(asset)
        self.trace_level += 1
        print(f"{self.name}: retrieved {asset.name} from {self.rig.name}.")
        return True

    def store_all_to_rig(self) -> bool:
        """Attempt to store all items from inventory into rig storage."""
        if not self.rig:
            print(f"{self.name}: no rig to store into.")
            return False
        moved = False
        for a in list(self._inventory):
            if self.rig.store_asset(a):
                self._inventory.remove(a)
                moved = True
        if moved:
            self.trace_level += 1
        return moved

    def retrieve_all_from_rig(self) -> bool:
        """Retrieve all non-encrypted assets from rig storage to inventory."""
        if not self.rig:
            print(f"{self.name}: no rig to retrieve from.")
            return False
        non_encrypted = [a for a in self.rig.storage if not a.encrypted]
        if not non_encrypted:
            print(f"{self.name}: no non-encrypted assets to retrieve.")
            return False
        for a in non_encrypted:
            self._inventory.append(a)
            print(f"{self.name}: retrieved {a.name} from {self.rig.name}.")
        self.rig.storage = [a for a in self.rig.storage if a.encrypted]
        self.trace_level += 1
        return True

    def reduce_trace(self, amount: int = 1):
        """Lower trace level by amount (not below 0)."""
        before = self.trace_level
        self.trace_level = max(0, self.trace_level - amount)
        print(f"{self.name}: trace reduced from {before} to {self.trace_level}.")

    def lay_low(self):
        """
        Basic way to reduce trace. If a CryptoToken is consumed, reduce more.
        """
        if self._consume_by_name("CryptoToken"):
            self.reduce_trace(3)
            print(f"{self.name}: used CryptoToken to lay low effectively.")
        else:
            self.reduce_trace(1)
            print(f"{self.name}: lay low reduced trace slightly.")