import cv2
import numpy as np

def draw_rectangles(img_np, positions):
    """Draw rectangles around the found text positions."""
    for pos in positions:
        x, y, w, h = pos
        img_np = cv2.rectangle(img_np, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return img_np