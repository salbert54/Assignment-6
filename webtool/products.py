
from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass, field
from enum import Enum, IntEnum
from typing import List, TypeAlias
from urllib.error import HTTPError
from xml.etree.ElementTree import Element, fromstring

import requests
from iniconfig import ParseError

class Products:
    product_id: int = ""
    product_brand: str = ""
    product_name: str = ""
    product_sku: int = ""

Products = [(1, "The Ordinary", "100% Organic Cold-Pressed Rose Hip Seed Oil", 2031417),
            (2, "La Mer", "The Renewal Oil", 1932649), 
            (3, "First Aid Beauty", "Ultra Repair Oat & Hemp Seed Dry Oil", 2166338), 
            (4, "Youth To The People", "Superberry Hydrate + Glow Dream Oil", 2067916), 
            (5, "Drunk Elephant", "Virgin Marula Luxury  Face Oil", 1679315), 
            (6, "Biossance", "100% Sugarcane Squalane Oil", 2051944), 
            (7, "Josie Maran", "100 percent Pure Argan Oil", 1121797)
            ]

class ProductComponents:
    pc_id: int = ""
    product_id: int = ""
    component_id: int = ""

class Components:
    component_id: int = ""
    component_name: str = ""
    component_irritating: bool = ""

Components = [(1, "Rosa Canina Seed Oil", False),
            (2, "100% Unrefined Sclerocraya Birrea (Marula) Kernel Oil", False),
            (3, "Argania Spinosa (Argan) Kernel Oil", False), 
            (4, "100% Squalane Oil", False),
            (5, "Helianthus Annuus (Sunflower) Seed Oil", False),
            (6, "Dicaprylyl Carbonate", False),
            (7, "Simmondsia Chinensis (Jojoba) Seed Oil", False),
            (8, "Tocopherol", False),
            (9, "Natural Fragrance", True),
            (10, "Linalool", True),
            (11, "Limonene", True),
            (12, "Citronellol", True),
            (13, "Citral", True),
            (14, "Amylcinnamyl Alcohol", True),
            (15, "Dimethicone", True),
            (16, "Alcohol Denat.", True),
            (17, "Fragrance", True), 
            (18, "Phenyl Trimethicone", True)]