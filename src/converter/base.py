"""
Base converter module - The brain of our conversion system.
"""

from typing import Dict, Callable
from .temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius
)
from .length import (
    meters_to_feet,
    feet_to_meters,
    km_to_miles,
    miles_to_km,
    cm_to_inches,
    inches_to_cm
)
from .weight import (
    kg_to_pounds,
    pounds_to_kg,
    grams_to_ounces,
    ounces_to_grams
)
from .volume import (
    liters_to_gallons,
    gallons_to_liters,
    ml_to_fl_oz,
    fl_oz_to_ml
)


class UnitConverter:
    """
    The brain of our conversion system. Clean, efficient, no nonsense.
    Each conversion method follows a predictable pattern - that's intentional.
    """
    
    def __init__(self):
        """Initialize with conversion mappings. Expandable by design."""
        self.conversions = self._build_conversion_map()
        
    def _build_conversion_map(self) -> Dict[str, Dict[str, Callable]]:
        """
        Central registry of all conversions. Want to add more? Just extend this.
        The structure is deliberate: category -> specific conversion -> function
        """
        return {
            'temperature': {
                'celsius_fahrenheit': celsius_to_fahrenheit,
                'fahrenheit_celsius': fahrenheit_to_celsius,
                'celsius_kelvin': celsius_to_kelvin,
                'kelvin_celsius': kelvin_to_celsius
            },
            'length': {
                'meters_feet': meters_to_feet,
                'feet_meters': feet_to_meters,
                'km_miles': km_to_miles,
                'miles_km': miles_to_km,
                'cm_inches': cm_to_inches,
                'inches_cm': inches_to_cm
            },
            'weight': {
                'kg_pounds': kg_to_pounds,
                'pounds_kg': pounds_to_kg,
                'grams_ounces': grams_to_ounces,
                'ounces_grams': ounces_to_grams
            },
            'volume': {
                'liters_gallons': liters_to_gallons,
                'gallons_liters': gallons_to_liters,
                'ml_fl_oz': ml_to_fl_oz,
                'fl_oz_ml': fl_oz_to_ml
            }
        }