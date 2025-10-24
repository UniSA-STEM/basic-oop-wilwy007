"""
File: Rig.py
Description: The Rig Class represents the Hackers computer. It handles storage, damage,
    broken state, upgrades and repairs. Each rig starts with two data Spikes and one
    removable drive.
Author: William Willoughby
ID: 110477792
Username: wilwy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from typing import List
import random
from Asset import Asset

class Rig:
    def __init__(self, name: str):
        self.name = name
        self.damage = 0
        self.broken = False
        self.storage: List[Asset] = []
        self.upgrade_level = 0

        self.storage.append(Asset("Data Spike", "For use in battles."))
        self.storage.append(Asset("Data Spike", "For use in battles."))
        self.storage.append(Asset("Removable Drive", "Found in rigs and used for extraction."))

def storage_capacity(self) -> int:
    """Base capacity increases with upgrade level."""
    base_capacity = 5
    return base_capacity + (self.upgrade_level * 2)

def hits_to_break(self) -> int:
    """Return the number of hits to break."""
    return 2 + self.upgrade_level

def take_hit(self):
    """Rig takes hit from Data Spike and becomes broken if damage reaches threshold"""
    if self.broken:
        print(f"{self.name}: Is already broken.")
        return
    self.damage += 1
    print(f"{self.name}: The rig is now at {self.damage} damage.")
    if self.damage >= self.hits_to_break():
        self.broken = True
        print(f"{self.name}: The rig is now broken!")

def repair(self, consumer_callable = None) -> bool:
    """Repair the Rig. If token is available repair."""
    if self.damage == 0 and not self.broken:
        print(f"{self.name}: No repair needed as the rig is not broken.")
        return False

    if consumer_callable:
        if not consumer_callable("CryptoToken"):
            print(f"{self.name}: Repair Failed! CryptoToken is not available.")
            return False

    self.damage = 0
    self.broken = False
    print(f"{self.name}: The rig is repaired and now at {self.damage} damage.")
    return True

def upgrade(self):
    """Upgrade by applying a Hardware Patch."""
    self.upgrade_level += 1
    self.damage = max(0, self.damage - 1)
    if self.damage < self.hits_to_break():
        self.broken = False
    print(f"{self.name}: Is now upgraded to level {self.upgrade_level}.")

def generate_assets(self) -> Asset:
    """
    Generate one asset randomly. if storage has room store  it and return asset
    else if storage full return asset but do not store.
    """
    choices = [
        Asset("Data Spike", "For use in battles."),
        Asset("Removable Drive", "Found in rigs and used for extraction."),
        Asset("CryptoToken", "Used to acquire or repair rigs."),
        Asset("Security Chip", "Used to encrypt or decrypt assets"),
        Asset("Hardware Patch", "Used to upgrade rigs")
    ]
    generated = random.choice(choices)
    if len(self.storage) < self.storage_capacity():
        self.storage.append(generated)
        print(f"{self.name}: generated {generated} asset and stored in storage.")
    else:
        print(f"{self.name}: Generated {generated} but storage is full.")
    return generated

def store_asset(self, asset: Asset) -> bool:
    """Store asset in storage if storage not full."""
    if len(self.storage) >= self.storage_capacity():
        print(f"{self.name}: Cannot store {asset} as storage is full.")
        return False
    self.storage.append(asset)
    print(f"{self.name}: Stored {asset} in storage.")
    return True

def release_asset(self, asset_name: str) -> Asset or None:
    """
    Release the first non-encrypted asset with matching name.
    If the asset is not encrypted, return None.
    """
    for i, a in enumerate(self.storage):
        if a.name == asset_name:
            if a.encrypted:
                print(f"{self.name}: {asset_name} is encrypted and cannot be released.")
                return None
            return self.storage.pop(i)
    print(f"{self.name}: Asset {asset_name} not found.")
    return None
