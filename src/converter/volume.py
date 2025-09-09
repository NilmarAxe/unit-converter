"""
Volume conversions - for the chemists and chefs.
"""


def liters_to_gallons(value: float) -> float:
    """Liters to gallons: Fuel economy calculations"""
    return value * 0.264172


def gallons_to_liters(value: float) -> float:
    """Gallons to liters: Global standard volume"""
    return value / 0.264172


def ml_to_fl_oz(value: float) -> float:
    """ML to fluid oz: Beverage industry standard"""
    return value * 0.033814


def fl_oz_to_ml(value: float) -> float:
    """Fluid oz to ML: Precise liquid measurements"""
    return value / 0.033814