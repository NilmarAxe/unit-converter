"""
Menu management module - Organized menu structure and display logic.
"""

from typing import Dict, Tuple


class MenuManager:
    """
    Handles all menu-related operations.
    Categories make sense, options are clear.
    """
    
    def create_menu_structure(self) -> Dict[str, Tuple]:
        """
        Organized menu structure. Categories make sense, options are clear.
        No ambiguity, no confusion. That's the goal.
        """
        return {
            '1': ('Temperature', [
                ('1', 'Celsius → Fahrenheit', 'celsius_fahrenheit'),
                ('2', 'Fahrenheit → Celsius', 'fahrenheit_celsius'),
                ('3', 'Celsius → Kelvin', 'celsius_kelvin'),
                ('4', 'Kelvin → Celsius', 'kelvin_celsius')
            ]),
            '2': ('Length', [
                ('1', 'Meters → Feet', 'meters_feet'),
                ('2', 'Feet → Meters', 'feet_meters'),
                ('3', 'Kilometers → Miles', 'km_miles'),
                ('4', 'Miles → Kilometers', 'miles_km'),
                ('5', 'Centimeters → Inches', 'cm_inches'),
                ('6', 'Inches → Centimeters', 'inches_cm')
            ]),
            '3': ('Weight', [
                ('1', 'Kilograms → Pounds', 'kg_pounds'),
                ('2', 'Pounds → Kilograms', 'pounds_kg'),
                ('3', 'Grams → Ounces', 'grams_ounces'),
                ('4', 'Ounces → Grams', 'ounces_grams')
            ]),
            '4': ('Volume', [
                ('1', 'Liters → Gallons', 'liters_gallons'),
                ('2', 'Gallons → Liters', 'gallons_liters'),
                ('3', 'Milliliters → Fluid Ounces', 'ml_fl_oz'),
                ('4', 'Fluid Ounces → Milliliters', 'fl_oz_ml')
            ])
        }
    
    def display_main_menu(self, menu_options: Dict):
        """Main menu. Clear categories, obvious choices."""
        print("\n▶ SELECT CATEGORY:")
        print("-" * 30)
        for key, (category, _) in menu_options.items():
            print(f"  [{key}] {category}")
        print("  [0] Exit")
        print("-" * 30)
    
    def display_category_menu(self, category_key: str, menu_options: Dict):
        """Category submenu. Logical groupings, clear navigation."""
        category_name, options = menu_options[category_key]
        print(f"\n▶ {category_name.upper()} CONVERSIONS:")
        print("-" * 30)
        for num, desc, _ in options:
            print(f"  [{num}] {desc}")
        print("  [0] Back to main menu")
        print("-" * 30)