import re

input_file_path = 'input.gcode'
output_file_path = 'output.gcode'

# Initialize variables
currentX = 0
currentY = 0
targetX = 0
targetY = 0
previousX = 0
previousY = 0
Xdirection = 0
Ydirection = 0
previousXdirection = 0
previousYdirection = 0
Xbacklash = 0.1  # Example value for x-axis backlash compensation
Ybacklash = 0.1  # Example value for y-axis backlash compensation

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        # Assuming G-code commands are in the format "G0 X12.5 Y7.3" or similar
        if line.startswith('G0') or line.startswith('G1'):
            targetX = float(re.findall(r'x(\d+\.\d+|\d+)', line)[0])
            targetY = float(re.findall(r'y(\d+\.\d+|\d+)', line)[0])
            print(f"targetX: {targetX}, targetY: {targetY}")
            print(f"currentX: {currentX}, currentY: {currentY}")
            print(f"previousX: {previousX}, previousY: {previousY}")
            
            # Check direction changes
            Xdirection = 1 if targetX > currentX else -1 if targetX < currentX else 0
            Ydirection = 1 if targetY > currentY else -1 if targetY < currentY else 0
            if Xdirection > previousXdirection and Xdirection!= 0:
                compX = round(currentX + Xbacklash, 3)
                comp = True
            elif Xdirection < previousXdirection and Xdirection!= 0:
                compX = round(currentX - Xbacklash, 3)
                comp = True
            if Ydirection > previousYdirection and Ydirection!= 0:
                compY = round(currentY + Ybacklash, 3)
                comp = True
            elif Ydirection < previousYdirection and Ydirection!= 0:
                compY = round(currentY - Ybacklash, 3)
                comp = True
            print(f"compX: {compX}, compY: {compY}")
            if comp:
                compLines = [f"G0 x{compX} y{compY} ; Compensation line", f"G92 x{currentX} y{currentY} ; Compensation line"]
                newLine = f"{compLines[0]}\n{compLines[1]}\n{line}"
            else:
                newLine = line
            previousX = currentX
            previousY = currentY
            currentX = targetX
            currentY = targetY
            previousXdirection = Xdirection
            previousYdirection = Ydirection
            comp = False
            
        else:
            newLine = line
        # Write the modified line to the output file
        output_file.write(newLine)

# Close the files
input_file.close()
output_file.close()
