"""
Output formatting module - Present results professionally.
Clarity is non-negotiable. Numbers should be readable, units should be obvious.
"""


class ResultFormatter:
    """
    Handles all output formatting operations.
    Professional presentation of conversion results.
    """
    
    def format_result(self, original: float, converted: float, 
                     from_unit: str, to_unit: str):
        """
        Present results professionally. Clarity is non-negotiable.
        Numbers should be readable, units should be obvious.
        """
        print("\n" + "="*50)
        print("CONVERSION RESULT:")
        print("-"*50)
        
        # Smart formatting based on magnitude
        if abs(converted) < 0.01 or abs(converted) > 10000:
            print(f"  {original:,.2f} {from_unit}")
            print(f"  ↓")
            print(f"  {converted:.4e} {to_unit}")
        else:
            print(f"  {original:,.2f} {from_unit}")
            print(f"  ↓")
            print(f"  {converted:,.4f} {to_unit}")
        
        print("="*50)