"""
The user-facing component. Clean, intuitive, error-resistant.
Good UX is just good logic applied to human interaction.
"""

import sys
from typing import Optional
from ..converter.base import UnitConverter
from .menu import MenuManager
from ..utils.validators import InputValidator
from ..utils.formatters import ResultFormatter


class Interface:
    """
    The user-facing component. Clean, intuitive, error-resistant.
    Good UX is just good logic applied to human interaction.
    """
    
    def __init__(self):
        self.converter = UnitConverter()
        self.menu_manager = MenuManager()
        self.input_validator = InputValidator()
        self.formatter = ResultFormatter()
        self.menu_options = self.menu_manager.create_menu_structure()
    
    def display_header(self):
        """First impressions matter. Even in CLI."""
        print("\n" + "="*50)
        print("     PROFESSIONAL UNIT CONVERTER")
        print("     Precision. Efficiency. Simplicity.")
        print("="*50)
    
    def perform_conversion(self, category: str, conversion_key: str, value: float) -> Optional[float]:
        """
        Execute the actual conversion. Clean delegation to the converter.
        Single responsibility principle in action.
        """
        try:
            conversion_func = self.converter.conversions[category][conversion_key]
            return conversion_func(value)
        except (KeyError, TypeError):
            return None
    
    def run(self):
        """
        Main application loop. State management done right.
        Clear flow, predictable behavior, graceful exits.
        """
        self.display_header()
        
        while True:
            self.menu_manager.display_main_menu(self.menu_options)
            
            category_choice = self.input_validator.get_user_input("Enter choice: ")
            
            if category_choice == '0':
                print("\n✓ Thank you for using Professional Unit Converter.")
                print("  Precision in every conversion.\n")
                break
            
            if category_choice not in self.menu_options:
                print("\n⚠ Invalid selection. Please choose a valid option.")
                continue
            
            # Category selected, show specific conversions
            category_name, conversions = self.menu_options[category_choice]
            category_key = category_name.lower()
            
            while True:
                self.menu_manager.display_category_menu(category_choice, self.menu_options)
                
                conversion_choice = self.input_validator.get_user_input("Select conversion: ")
                
                if conversion_choice == '0':
                    break
                
                # Find the selected conversion
                selected = None
                for num, desc, key in conversions:
                    if num == conversion_choice:
                        selected = (desc, key)
                        break
                
                if not selected:
                    print("\n⚠ Invalid selection. Please try again.")
                    continue
                
                desc, conversion_key = selected
                
                # Get the value to convert
                print(f"\n▶ {desc}")
                value = self.input_validator.get_user_input("Enter value to convert: ", float)
                
                if value is None:
                    print("\n⚠ Invalid input. Please enter a valid number.")
                    continue
                
                # Perform conversion
                result = self.perform_conversion(category_key, conversion_key, value)
                
                if result is None:
                    print("\n⚠ Conversion error. Please try again.")
                    continue
                
                # Extract units from description
                units = desc.split(' → ')
                from_unit = units[0].split()[-1] if len(units) > 0 else ""
                to_unit = units[1] if len(units) > 1 else ""
                
                self.formatter.format_result(value, result, from_unit, to_unit)
                
                # Ask if user wants another conversion
                another = self.input_validator.get_user_input("\nPerform another conversion? (y/n): ")
                if another and another.lower() != 'y':
                    break