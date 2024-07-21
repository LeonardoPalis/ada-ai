from PIL import Image
import cv2
import numpy as np

def load_image(img_path):
    img = Image.open(img_path)
    return np.array(img)

def convert_to_grayscale(img_np):
    return cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

def save_image(img_np, output_image_path):
    cv2.imwrite(output_image_path, img_np)