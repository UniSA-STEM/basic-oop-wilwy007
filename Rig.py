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

