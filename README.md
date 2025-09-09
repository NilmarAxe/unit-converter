# Unit Converter

## Overview

This repository hosts a precise and extensible unit conversion tool implemented in Python. It supports conversions across essential categories including length, mass, volume, temperature, time, area, speed, energy, and pressure. Designed for efficiency, it eliminates the need for error-prone manual calculations or unreliable online services, providing a robust offline solution suitable for integration into scripts, applications, or standalone use.

The architecture prioritizes modularity and maintainability, allowing seamless extension to new units or categories without disrupting core functionality.

## Features

- **Comprehensive Coverage**: Handles conversions in key measurement domains with high accuracy.
- **Precision Control**: Utilizes numerical libraries for exact results, with configurable rounding.
- **Modular Design**: Category-specific modules enable targeted modifications or expansions.
- **CLI and Interactive Modes**: Supports command-line arguments for quick conversions and an interactive shell for multiple operations.
- **API Integration**: Exposes a simple interface for programmatic use in custom projects.
- **Error Handling**: Validates inputs to prevent invalid operations, ensuring reliability.
- **Cross-Platform**: Compatible with Windows, macOS, and Linux environments.
- **Testing**: Includes unit tests to verify conversion accuracy.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/NilmarAxe/unit-converter.git
   cd unit-converter
   ```

2. Create and activate a virtual environment:
   - Unix/macOS: `python -m venv venv && source venv/bin/activate`
   - Windows: `python -m venv venv && venv\Scripts\activate`

3. Install dependencies (requires Python 3.8+):
   ```
   pip install -r requirements.txt
   ```

4. Verify setup:
   ```
   python main.py --help
   ```

## Usage

### Command-Line
Perform a single conversion:
```
python main.py <value> <from_unit> <to_unit>
```
Example: Convert 5 kilometers to miles
```
python main.py 5 km miles
```

### Interactive Mode
For multiple conversions:
```
python main.py --interactive
```
Follow prompts to input values and units.

### API Integration
Import and use programmatically:
```python
from converter import UnitConverter

converter = UnitConverter()
result = converter.convert(5, 'km', 'miles')
print(result)  # Outputs the converted value
```

### Advanced Options
- Specify precision: Add `--precision <digits>` to CLI commands.
- Batch processing: Pipe inputs or integrate into scripts for automation.

## Code Structure

- `main.py`: Handles entry points and user interfaces.
- `converter.py`: Core conversion logic and unit mappings.
- `units/`: Modular files for each category (e.g., `length.py`).
- `utils.py`: Utility functions for validation and formatting.
- `tests/`: Automated tests for reliability.

## Development Choices

Python was selected for its optimal balance of readability and computational efficiency in handling mathematical operations. The modular structure facilitates future-proofing, allowing independent updates to categories without systemic refactoring.

## Contributing

Contributions are evaluated based on their alignment with project goals: precision, efficiency, and extensibility. 
- Fork the repository.
- Create a feature branch.
- Submit a pull request with clear, logical commit messages.
- Ensure tests pass and add new ones for changes.

Adhere to PEP 8 standards. Focus on impactful improvements over superficial changes.

## License

MIT License. See `LICENSE` for details.

## Acknowledgments

Built to address practical needs in scientific, engineering, and educational contexts. No unnecessary dependencies; efficiency is paramount.
