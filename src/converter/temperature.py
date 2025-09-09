"""
Temperature conversion functions - the classics everyone needs.
"""


def celsius_to_fahrenheit(value: float) -> float:
    """C to F: The most requested conversion in the US"""
    return (value * 9/5) + 32


def fahrenheit_to_celsius(value: float) -> float:
    """F to C: For when Americans travel abroad"""
    return (value - 32) * 5/9


def celsius_to_kelvin(value: float) -> float:
    """C to K: For the scientists among us"""
    return value + 273.15


def kelvin_to_celsius(value: float) -> float:
    """K to C: Back to human-readable temperatures"""
    return value - 273.15