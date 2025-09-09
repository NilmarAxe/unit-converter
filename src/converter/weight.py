"""
Weight conversions - gym enthusiasts rejoice.
"""


def kg_to_pounds(value: float) -> float:
    """Kg to lbs: The eternal fitness question"""
    return value * 2.20462


def pounds_to_kg(value: float) -> float:
    """Lbs to kg: International weight standard"""
    return value / 2.20462


def grams_to_ounces(value: float) -> float:
    """Grams to oz: Kitchen precision"""
    return value * 0.035274


def ounces_to_grams(value: float) -> float:
    """Oz to grams: Baking accuracy matters"""
    return value / 0.035274