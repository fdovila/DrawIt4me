# 290120242136 c01725a4cfee5001
################
# DRAW IT FOR ME
################
# By F.B. Avila-Rencoret, MD. 2024,CCBYNC4.0
# A tool for drawing wireframes in [INSERT WHATEVER APP] using a any image as input.
# NO AI required. Just a simple image processing script that converts the image into mouse strokes.
# THE KEY SECRET IS SWITCHING BETWEEN THE TERMINAL WINDOW AND YOUR APP USING ALT+TAB
# The script will ask you to select the target window (via terminal UX), then capture the positions of the drawing and selection tools.
# Then it will ask you to define the ROI (region of interest) by clicking and dragging.


import tkinter as tk
from tkinter import filedialog
import pygetwindow as gw
import pyautogui
import cv2
import numpy as np
from pynput import keyboard, mouse

def get_image_path():
    root = tk.Tk()
    root.withdraw()
    image_path = filedialog.askopenfilename(title="Select Wireframe Image")
    return image_path

def select_target_window():
    titles = gw.getAllTitles()
    windows = {i: title for i, title in enumerate(titles) if title}
    for idx, title in windows.items():
        print(f"{idx}: {title}")

    selected_index = int(input("Enter the number of the target window: "))
    window = gw.getWindowsWithTitle(windows[selected_index])[0]
    return window

def capture_tool_positions():
    positions = {}
    def on_click(x, y, button, pressed):
        if not pressed:
            if 'drawing_tool' not in positions:
                positions['drawing_tool'] = (x, y)
                print("Drawing tool position captured.")
            elif 'selection_tool' not in positions:
                positions['selection_tool'] = (x, y)
                print("Selection tool position captured.")
                return False

    with mouse.Listener(on_click=on_click) as listener:
        print("Click to capture the drawing tool position, then the selection tool position.")
        listener.join()

    return positions['drawing_tool'], positions['selection_tool']

def define_roi():
    start_pos, end_pos = None, None
    def on_click(x, y, button, pressed):
        nonlocal start_pos, end_pos
        if pressed and not start_pos:
            start_pos = (x, y)
        elif not pressed and start_pos:
            end_pos = (x, y)
            return False

    with mouse.Listener(on_click=on_click) as listener:
        print("Define the ROI by clicking and dragging.")
        listener.join()

    return start_pos, end_pos

def process_image(image_path):
    image = cv2.imread(image_path, 0)
    _, binary = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    paths = []
    for contour in contours:
        if len(contour) > 1:
            path = []
            for point in contour:
                path.append((point[0][0], point[0][1]))
            paths.append(path)
    return paths, image.shape

def convert_to_mouse_strokes(paths, image_shape, roi, window):
    left, top, right, bottom = roi
    width, height = right - left, bottom - top
    image_width, image_height = image_shape[1], image_shape[0]

    window.activate()

    for path in paths:
        for i, (x, y) in enumerate(path):
            scaled_x = (x / image_width) * width
            scaled_y = (y / image_height) * height
            mapped_x = left + scaled_x
            mapped_y = top + scaled_y

            if i == 0:
                pyautogui.moveTo(mapped_x, mapped_y)
            else:
                pyautogui.dragTo(mapped_x, mapped_y, duration=0.1)

def main():
    try:
        image_path = get_image_path()
        window = select_target_window()
        drawing_tool_pos, selection_tool_pos = capture_tool_positions()

        print("Press Ctrl+Shift to start ROI definition.")
        with keyboard.GlobalHotKeys({'<ctrl>+<shift>': lambda: print("Define the ROI now.")}):
            start_pos, end_pos = define_roi()

        roi = (start_pos[0], start_pos[1], end_pos[0], end_pos[1])
        paths, image_shape = process_image(image_path)

        # Activate the drawing tool
        window.activate()
        pyautogui.click(drawing_tool_pos[0], drawing_tool_pos[1])

        # Start the drawing process
        convert_to_mouse_strokes(paths, image_shape, roi, window)
        print("Drawing complete.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
