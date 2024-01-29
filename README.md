# Automated Drawing any Pict Anywhere
By. F.B. Avila-Rencoret

## Overview
This Python script automates the process of drawing a wireframe image within a specified region of interest (ROI) in a drawing application. It allows users to select a target window, define the positions of drawing and selection tools, specify an ROI, and then automatically draws the wireframe image within that region.

## Features
- Select a target window from currently active applications.
- Capture positions of the drawing and rectangular selection tools.
- Define ROI with click-and-drag action.
- Automatic conversion of a wireframe image into mouse strokes within the ROI.

## Prerequisites
- Python 3.x
- Libraries: `pygetwindow`, `pyautogui`, `opencv-python`, `numpy`, `pynput`
- A wireframe image file

## Installation
Install the required Python libraries using pip:
```
pip install -r requirements. txt
```
## Usage
- Open you fav drawing tool, e.g. MS Paint. Predefine the size of your canvas, the type od drawing and thickeness and colour.
- Run the script from your terminal or from your fav IDE.
- Select the target window from the list of active windows. (use the number corresponding to your target app in the numeric menu).
- Click once to set the position of the **drawing tool**, and click again to set the position of the **rectangular selection tool** in the drawing application.
- Press Ctrl+Shift and then define the ROI in the drawing application by clicking and dragging (using the selections tool which should be active).
- The script will automatically process the wireframe image and draw it within the ROI.
  
## Limitations
- The script is designed for use with specific drawing applications and may require adjustments for different software.
- Accurate ROI definition and tool position capture are crucial for the correct functioning of the script.

## Future
- The image processing with openCV is quite simple. There are many ways to improve the image to edges conversion.

## License
[CC BY-NC 4.0, Attribution-NonCommercial 4.0 International]([https://pages.github.com/](https://creativecommons.org/licenses/by-nc/4.0/)https://creativecommons.org/licenses/by-nc/4.0/)
