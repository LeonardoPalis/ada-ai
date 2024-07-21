from image_processing import load_image, convert_to_grayscale, save_image
from ocr_processing import perform_ocr, find_text_positions
from drawing import draw_rectangles

def main():
    img_name = "screen_github.png"
    img_path = f"./debug/inputs/{img_name}"
    output_image_path = f"./debug/outputs/recognized_{img_name}"
    text_to_find = "Deploy keys"

    img_np = load_image(img_path)
    gray_img = convert_to_grayscale(img_np)

    ocr_result = perform_ocr(gray_img)
    positions = find_text_positions(ocr_result, text_to_find)

    img_with_rectangles = draw_rectangles(img_np, positions)
    save_image(img_with_rectangles, output_image_path)

    print(positions)

if __name__ == "__main__":
    main()