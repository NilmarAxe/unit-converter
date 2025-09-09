# Unit Converter

## Overview

This repository houses a comprehensive unit conversion tool engineered for accuracy, efficiency, and extensibility. In a world where measurements span diverse systems—imperial, metric, and specialized domains—having a reliable converter is essential for professionals, educators, and enthusiasts alike. This application streamlines the process of translating values across categories such as length, mass, volume, temperature, time, and more, eliminating the need for manual calculations or unreliable online tools. Built with a logical architecture that prioritizes clean code and modular components, it ensures long-term maintainability and adaptability to future requirements.

The core philosophy behind this tool is to provide a no-nonsense solution that delivers precise results without unnecessary complexity. By leveraging standardized conversion factors and handling edge cases methodically, it minimizes errors that could arise from floating-point arithmetic or unit mismatches. Whether you're integrating it into a larger system or using it standalone, the design emphasizes strategic foresight, allowing users to focus on their objectives rather than wrestling with implementation details.

## Features

- **Broad Unit Support**: Covers essential categories including:
  - Length (e.g., meters to feet, kilometers to miles)
  - Mass (e.g., kilograms to pounds, grams to ounces)
  - Volume (e.g., liters to gallons, cubic meters to cubic feet)
  - Temperature (e.g., Celsius to Fahrenheit, Kelvin to Celsius)
  - Time (e.g., seconds to minutes, hours to days)
  - Area (e.g., square meters to square feet, hectares to acres)
  - Speed (e.g., km/h to mph, m/s to ft/s)
  - Energy (e.g., joules to calories, kWh to BTU)
  - Pressure (e.g., pascals to psi, bar to atm)

- **High Precision Handling**: Utilizes robust numerical libraries to manage conversions with minimal loss of accuracy, incorporating rounding options where appropriate.

- **Modular Architecture**: Each conversion category is encapsulated in its own module, facilitating easy additions or modifications without disrupting the overall system.

- **Command-Line Interface (CLI)**: A straightforward CLI for quick conversions, ideal for scripting or batch processing.

- **Extensibility**: Simple API for developers to integrate into custom applications, with clear hooks for adding new units or categories.

- **Error Handling**: Intelligent validation to prevent invalid conversions, such as mixing incompatible units, with informative feedback.

- **Cross-Platform Compatibility**: Runs seamlessly on Windows, macOS, and Linux environments.

This set of features was selected to address common pain points in unit conversion tasks, ensuring the tool remains versatile yet focused on delivering value efficiently.

## Installation

To get started, clone the repository and set up the environment. The project is implemented in Python, chosen for its balance of readability and performance in mathematical operations.

1. **Clone the Repository**:
   ```
   git clone https://github.com/NilmarAxe/unit-converter.git
   cd unit-converter
   ```

2. **Set Up a Virtual Environment** (recommended for isolation):
   ```
   python -m venv venv
   source venv/bin/activate  # On Unix-based systems
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**:
   The project relies on minimal external libraries to keep it lightweight. Install them via:
   ```
   pip install -r requirements.txt
   ```
   Note: If `requirements.txt` includes libraries like `numpy` for advanced calculations, ensure your Python version is 3.8 or higher.

4. **Verify Installation**:
   Run a simple test:
   ```
   python main.py --help
   ```
   This should display usage instructions, confirming the setup.

This installation process is streamlined to minimize setup time, reflecting a strategic approach to user onboarding.

## Usage

The tool is designed for intuitive operation, with options for both interactive and non-interactive modes.

### Command-Line Usage

Invoke the script with parameters for direct conversions:

- Basic Syntax:
  ```
  python main.py <value> <from_unit> <to_unit>
  ```

- Examples:
  - Convert 5 kilometers to miles:
    ```
    python main.py 5 km miles
    ```
    Output: `5 km is approximately 3.10686 miles.`

  - Convert 100 Fahrenheit to Celsius:
    ```
    python main.py 100 f c
    ```
    Output: `100 F is approximately 37.7778 C.`

  - Convert 2.5 liters to gallons:
    ```
    python main.py 2.5 l gal
    ```
    Output: `2.5 l is approximately 0.66043 gal.`

For a full list of supported units, use:
```
python main.py --list-units
```

### Interactive Mode

Launch an interactive shell for multiple conversions:
```
python main.py --interactive
```
Follow prompts to input values and units, ideal for exploratory use.

### API Integration

For developers, import the converter as a module:

```python
from converter import UnitConverter

converter = UnitConverter()
result = converter.convert(10, 'kg', 'lb')
print(result)  # Outputs: 22.0462
```

This API is crafted with a focus on simplicity and predictability, allowing seamless incorporation into workflows.

### Advanced Options

- **Precision Control**: Specify decimal places:
  ```
  python main.py 3.14159 m ft --precision 2
  ```
  Output: `3.14159 m is approximately 10.30 ft.`

- **Batch Processing**: Pipe inputs from a file for bulk conversions.

These options ensure the tool adapts to varying levels of complexity without overcomplicating the core functionality.

## Code Structure

The codebase is organized logically to promote clarity and scalability:

- **`main.py`**: Entry point handling CLI arguments and interactive mode.
- **`converter.py`**: Core logic with conversion functions and unit mappings.
- **`units/`**: Directory containing category-specific modules (e.g., `length.py`, `mass.py`).
- **`utils.py`**: Helper functions for validation, rounding, and error handling.
- **`tests/`**: Unit tests to verify accuracy across conversions.
- **`requirements.txt`**: Dependency list.
- **`LICENSE`**: MIT License details.

This structure was chosen to isolate concerns, making it easier to debug, test, and expand. For instance, adding a new category involves creating a new module in `units/` and registering it in `converter.py`—a process that takes minutes rather than hours.

## Development and Design Choices

The project employs a dictionary-based mapping for units and factors, ensuring constant-time lookups for efficiency. Temperature conversions handle non-linear scales appropriately. Floating-point issues are mitigated through careful use of decimal arithmetic where precision is critical.

Testing is integral, with coverage for common and edge cases, such as zero values, negative inputs (where applicable), and unit aliases (e.g., 'metres' for 'meters').

Future enhancements could include GUI support via Tkinter or web deployment with Flask, but the current focus remains on a solid CLI foundation to build upon strategically.

## Contributing

Contributions are welcome to enhance functionality or fix issues. Follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/new-unit`.
3. Commit changes: `git commit -m "Add support for pressure units"`.
4. Push to the branch: `git push origin feature/new-unit`.
5. Open a pull request with a clear description of changes and rationale.

Adhere to PEP 8 style guidelines for Python code. Include tests for new features to maintain reliability.

This contribution process is designed to encourage thoughtful additions that align with the project's long-term vision.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details. This permissive license allows broad use while protecting the core integrity of the work.

## Acknowledgments

Inspired by the need for a dependable, offline conversion tool in technical fields. Special thanks to open-source communities for foundational libraries that enable precise computations.

This unit converter represents a calculated effort to solve a perennial problem with elegance and foresight, ensuring it serves users effectively now and in the future.
