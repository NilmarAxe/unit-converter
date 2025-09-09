"""
Input validation module - Robust input handling.
Users make mistakes - we handle them gracefully.
"""

import sys
from typing import Optional, Any


class InputValidator:
    """
    Handles all input validation and user interaction.
    Expects the unexpected.
    """
    
    def get_user_input(self, prompt: str, input_type: type = str) -> Optional[Any]:
        """
        Robust input handling. Expects the unexpected.
        Users make mistakes - we handle them gracefully.
        """
        try:
            user_input = input(prompt).strip()
            
            if input_type == float:
                # Handle comma as decimal separator (international users)
                user_input = user_input.replace(',', '.')
                return float(user_input)
            elif input_type == int:
                return int(user_input)
            else:
                return user_input
                
        except ValueError:
            return None
        except KeyboardInterrupt:
            print("\n\n✓ Program terminated by user.")
            sys.exit(0)
        except Exception:
            return None