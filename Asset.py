"""
File: Asset.py
Description: The Asset Class represents the digital assets used in the simulation
    and each asset has a name, description and encrypted boolean flag.
Author: William Willoughby
ID: 110477792
Username: wilwy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Asset:
    def __init__(self, name, description, encrypted: bool = False):
        self.name = name
        self.description = description
        self.encrypted = encrypted
    def __str__(self) -> str:
        """Return a string representation of the Asset."""
        base = f"{self.name}: {self.description}"
        return f"{base} [Encrypted]" if self.encrypted else base
    def encrypt(self):
        """Encrypt the Asset."""
        self.encrypted = True
    def decrypt(self):
        """Decrypt the Asset."""
        self.encrypted = False