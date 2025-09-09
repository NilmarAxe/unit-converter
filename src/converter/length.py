"""
Length conversions - because the metric system makes sense.
"""


def meters_to_feet(value: float) -> float:
    """Meters to feet: Architecture's favorite"""
    return value * 3.28084


def feet_to_meters(value: float) -> float:
    """Feet to meters: When precision matters"""
    return value / 3.28084


def km_to_miles(value: float) -> float:
    """Km to miles: Road trip essential"""
    return value * 0.621371


def miles_to_km(value: float) -> float:
    """Miles to km: The rest of the world's perspective"""
    return value / 0.621371


def cm_to_inches(value: float) -> float:
    """Cm to inches: For detailed work"""
    return value / 2.54


def inches_to_cm(value: float) -> float:
    """Inches to cm: Precision in small measures"""
    return value * 2.54