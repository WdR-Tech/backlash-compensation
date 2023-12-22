from ..Script import Script
import re

class BacklashCompensationCura(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name": "Backlash Compensation",
            "key": "BacklashCompensation",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "x_backlash":
                {
                    "label": "X Backlash",
                    "description": "The amount of backlash compensation for the X axis.",
                    "unit": "mm",
                    "type": "float",
                    "default_value": 0.1
                },
                "y_backlash":
                {
                    "label": "Y Backlash",
                    "description": "The amount of backlash compensation for the Y axis.",
                    "unit": "mm",
                    "type": "float",
                    "default_value": 0.1
                }
            }
        }"""

    def execute(self, data):
        x_backlash = self.getSettingValueByKey("x_backlash")
        y_backlash = self.getSettingValueByKey("y_backlash")

        currentX = 0
        currentY = 0
        targetX = 0
        targetY = 0
        Xdirection = 0
        Ydirection = 0
        previousXdirection = 0
        previousYdirection = 0
        comp = False

        for layer_number, layer in enumerate(data):
            lines = layer.split("\n")
            for line_number, line in enumerate(lines):
                if line.startswith('G0 ') or line.startswith('G1 '):
                    try:
                        targetX = float(re.findall(r'X(\d+\.\d+|\d+)', line)[0])
                    except IndexError:
                        targetX = currentX
                    try:
                        targetY = float(re.findall(r'Y(\d+\.\d+|\d+)', line)[0])
                    except IndexError:
                        targetY = currentY

                    Xdirection = 1 if targetX > currentX else -1 if targetX < currentX else 0
                    Ydirection = 1 if targetY > currentY else -1 if targetY < currentY else 0
                    if Xdirection > previousXdirection and Xdirection != 0:
                        compX = round(currentX + x_backlash, 3)
                        comp = True
                    elif Xdirection < previousXdirection and Xdirection != 0:
                        compX = round(currentX - x_backlash, 3)
                        comp = True
                    else:
                        compX = currentX
                    if Ydirection > previousYdirection and Ydirection != 0:
                        compY = round(currentY + y_backlash, 3)
                        comp = True
                    elif Ydirection < previousYdirection and Ydirection != 0:
                        compY = round(currentY - y_backlash, 3)
                        comp = True
                    else:
                        compY = currentY

                    if comp:
                        compLines = [f"G0 X{compX} Y{compY} ; Compensation line", f"G92 X{currentX} Y{currentY} ; Compensation line"]
                        newLine = f"{compLines[0]}\n{compLines[1]}\n{line}"
                        lines[line_number] = newLine
                        comp = False
                    currentX = targetX
                    currentY = targetY
                    previousXdirection = Xdirection
                    previousYdirection = Ydirection
                else:
                    lines[line_number] = line
            data[layer_number] = "\n".join(lines)

        return data
