### Columbia University in the City of New York
### The Fu Foundation School of Engineering and Applied Science
### Digital Manufacturing

# SVG Generator in Python (Laser Cut Box)

## Executive Summary

The goal of this assignment was to perform software-driven fabrication. We wrote a program that will generate a cardboard layout for folding an open-bin box. In the program, the user enters the dimensions of the material and the desired bin box. The software then generates an SVG file, which is then imported into a laser-cutter software and used to cut cardboard sheets to be folded into a box.

## Software Description

### Laser Cutter

The maximum possible dimensions of any box and material were the defined as the work area of the laser cutter in the Makerspace (Thunder Laser Nova51).
Length = 51.2, Width = 35.4, and Height = 9.1.

### Material

When the python script is run, the user is asked to input the length, width and thickness of the material they are expecting to cut. This user input is first checked to make sure there are no negative values or zeros. Then, the material dimensions were compared to the laser cutter work area to make sure they are within the maximum cutting area.

### Box

Next, the user is asked to enter the desired box length, width and height. These values are also checked to make sure there are no negative values or zeros and to make sure make sure that the box dimensions are less than the material dimensions.

### Folds and Flaps

The fold height was calculated to be the lesser of the (box width or box height) divided by 6.
The flap height was calculated to be the same as the fold height.
The flap width was calculated to be the lesser of the (box length or box height) divided by 2.

### Parameters

Our design has the entire box (with flaps and lid) to be cut from the same material. Therefore, the total length of the box that needs to fit on the material length was calculated as follows:
_total\_length = box\_length + (max(box\_height,(fold\_height+(flap\_height\*2)))\*2)_

Similarly, the total width of the box that needs to fit on the material length was as follows:
_total\_width = (box\_width\*2) + (box\_height\*2) + fold\_height + (flap\_height\*2)_

If the total box length was greater than the material length, or the total box width was greater than the material width, then the software would print an error and prompt the user to enter new values.

The minimum dimensions of this box were defined to be 2&quot;x2&quot;x2&quot;. If a user enters any values less than 2&quot; then the software would print an error and prompt the user to enter new values.

### Handles

The software automatically calculated the position and dimensions of the box handles. These handles were placed on the sides of the box and were dependent on the box height and box width. The edges of the box were rounded and the handle was placed below the fold height, for when the lid folds onto the sides of the box.

### Fold Lines

The fold lines were automatically calculated based on the box outline. The thickness of the fold line was equal to the material thickness, so that the box can be folded without the two sides of the material overlapping and damaging each other.

### Output

The software outputs an SVG file with all the formatting that is required to make an SVG file (header, footers and descriptions) and the code for the box outline, fold lines, designs, text, and handles.

The laser cutter is only able to set different speeds and laser strengths per color. Therefore, we selected three colors for our box design.
- Green: The box outline and handles were a &quot;cut&quot; with slowest speed and most intense laser strength. The laser is supposed to cut through the material to separate the box at the green lines.
- Red: The fold lines were a &quot;cut&quot; with a faster speed and less intense laser strength. The laser is supposed to cut through half of the material to allow the material to fold.
- Blue: The designs and text were a &quot;cut&quot; with the fastest speed and least intense laser strength. The laser is supposed to engrave the designs and text onto the material.
