# Backlash Compensation for Marlin 3D Printers

This project aims to address the lack of built-in backlash compensation in 3d printers that use marlin firmware older then marlin 2.0. by providing two different methods for incorporating backlash compensation into the printing process.

## Overview

- **Compatibility:** Primarily developed for older Marlin 3D printers lacking native support for backlash compensation.
- **Current Status:** This project is in the development phase, and users are advised to exercise caution as it may contain bugs. Use it at your own risk.

## Method 1: Cura Post-Processing Script
To use backlash compensation as a Cura post-processing script, follow these steps:

1. **Download the Script:**
   - Download the `BacklashCompensationCura.py` script from this repository.

2. **Copy the Script:**
   - Open File Explorer and navigate to `C:\Users\<user>\AppData\Roaming\cura\<version_number>\scripts\`.
   - Copy the downloaded `BacklashCompensationCura.py` script to this folder.

3. **How to Use:**
   - Restart Cura and go to `Extensions` > `Post Processing` > `Modify G-Code`.
   - Click on `Add a script` and select `Script` > `Backlash Compensation`.
   - Adjust the `X Backlash` and `Y Backlash` variables in the script to your backlash values in mm.
   - Click on "close".
   - Slice your model as usual, and the backlash compensation will be applied during post-processing.

## Method 2: Python Script
To implement backlash compensation using the Python script, follow these steps:

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
