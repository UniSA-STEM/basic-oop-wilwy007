"""
File: main.py
Description: Main code to run scenario tests for the assignment.
    Includes edge cases and normal flows to demonstrate the system.
Author: William Willoughby
ID: 110477792
Username: wilwy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random
random.seed(1)  # deterministic behaviour for repeatable tests

from Asset import Asset
from Rig import Rig
from Hacker import Hacker

def run_scenarios():
    print("=== Setup ===")
    william = Hacker("Warz")
    scott = Hacker("Scootz")

    print(william)
    print(scott)

    # Edge case: try to upgrade without a rig
    print("\n--- Edge: upgrade without rig ---")
    william.upgrade_rig()

    # Edge case: encrypt without a Security Chip
    print("\n--- Edge: encrypt without Security Chip ---")
    william.encrypt_asset("CryptoToken", location="inventory")

    # Acquire rig (William has a starter CryptoToken)
    print("\n--- William acquires rig ---")
    william.acquire_rig(Rig("Warzgamez"))
    print(william.rig)

    # Scott attempts to acquire after consuming his crypto (simulate failure)
    print("\n--- Scott loses token and tries to acquire rig ---")
    scott.scan_inventory_for("CryptoToken")  # consumes his starter token
    scott.acquire_rig(Rig("Scooterz"))

    # Generate items on William's rig and retrieve them
    print("\n--- Rig generates assets ---")
    william.rig.generate_assets()
    william.rig.generate_assets()
    william.rig.generate_assets()
    print("\n--- William retrieves non-encrypted items ---")
    william.retrieve_all_from_rig()
    print(william)

    # Give William a Security Chip and encrypt an asset
    print("\n--- Provide Security Chip and encrypt an asset ---")
    william.add_to_inventory(Asset("Security Chip", "Used for encryption/decryption"))
    # Try to encrypt one of the inventory items (CryptoToken maybe not present - safe check)
    # We'll encrypt the first non-encrypted asset we find
    for item in list(william._inventory):
        if not item.encrypted:
            william.encrypt_asset(item.name, location="inventory")
            break

    # Store encrypted asset into rig
    print("\n--- Store an asset (possibly encrypted) into rig ---")
    if william._inventory:
        william.store_to_rig(william._inventory[0].name)
    print(william.rig)

    # Battle: William attacks a neutral target rig until it breaks
    print("\n--- Battle: William attacks Dummyrig ---")
    target = Rig("Dummyrig")
    while not target.broken:
        # ensure William has a data spike to launch
        if not any(a.name == "Data Spike" for a in william.rig.storage):
            william.rig.storage.append(Asset("Data Spike", "For use in battles."))
        william.launch_data_spike(target)
        if william.trace_level > 10:  # safety to avoid infinite loop
            print("Trace too high — stopping attacks.")
            break

    # Add unsecured asset to target and attempt extraction without removable drive
    print("\n--- Extraction - attempt without Removable Drive ---")
    target.storage.append(Asset("Data Spike", "For use in battles."))
    william.extract_unsecured(target)

    # Give William a Removable Drive and extract
    print("\n--- Extraction - provide Removable Drive and extract ---")
    william.add_to_inventory(Asset("Removable Drive", "Used to extract unsecured files"))
    william.extract_unsecured(target)
    print(william)

    # Upgrade rig without patch (should fail)
    print("\n--- Upgrade attempt without Hardware Patch ---")
    william.upgrade_rig()

    # Give hardware patch and upgrade
    print("\n--- Provide Hardware Patch and upgrade ---")
    william.add_to_inventory(Asset("Hardware Patch", "Used to upgrade rigs"))
    william.upgrade_rig()
    print(william.rig)

    # Damage and repair rig
    print("\n--- Damage and repair ---")
    william.rig.damage = william.rig.hits_to_break()
    william.rig.broken = True
    william.add_to_inventory(Asset("CryptoToken", "Repair token"))
    william.upgrade_rig()
    print(william.rig)

    # Trace blocking demo
    print("\n--- Trace blocking demo ---")
    william.trace_level = 6
    william.launch_data_spike(target)  # should be blocked
    william.lay_low()
    william.launch_data_spike(target)  # may or may not succeed depending on trace

    print("\n=== Tests complete ===")

if __name__ == "__main__":
    run_scenarios()
