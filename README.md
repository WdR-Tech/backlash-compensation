# Backlash Compensation for Marlin 3D Printers

This project addresses the lack of built-in backlash compensation in older Marlin 3D printers by providing a Python script that can be integrated into the G-code workflow. Backlash compensation is crucial for minimizing inaccuracies caused by mechanical play in the printer's movement.

## Overview

- **Compatibility:** Primarily developed for older Marlin 3D printers lacking native support for backlash compensation.
- **Current Status:** This project is in the development phase, and users are advised to be cautious as it may contain bugs. Use it at your own risk.

## Getting Started

To implement backlash compensation using this script, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/backlash-compensation.git
   cd backlash-compensation
   ```

2. **Usage:**
   - Adjust the `input_file_path` and `output_file_path` variables in the script according to your G-code files.
   - Adjust the `Xbacklash` and `Ybacklash` variables to your backlash values in mm.
   - Run the script:
     ```bash
     python backlash_compensation.py
     ```

3. **Important Note:**
   - Ensure that you thoroughly test the generated G-code on a non-critical print before using it for important projects.

## Contributing

Contributions and feedback are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Disclaimer

This software is still in the development phase, and it is not guaranteed to be free of bugs. Use it at your own risk. The developers and contributors are not responsible for any potential issues that may arise from its use.

---
