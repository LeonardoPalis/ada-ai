import pytesseract

def perform_ocr(gray_img):
    """Perform OCR on a grayscale image."""
    return pytesseract.image_to_data(gray_img, output_type=pytesseract.Output.DICT)

def find_text_positions(ocr_result, text_to_find):
    """Find positions of the specified text in the OCR result."""
    positions = []
    for i in range(len(ocr_result["text"])):
        concatenated_text = ""
        for j in range(i, len(ocr_result["text"])):
            if concatenated_text:
                concatenated_text += " " + ocr_result["text"][j]
            else:
                concatenated_text = ocr_result["text"][j]

            if concatenated_text == text_to_find:
                x = ocr_result["left"][i]
                y = ocr_result["top"][i]
                w = ocr_result["left"][j] + ocr_result["width"][j] - ocr_result["left"][i]
                h = max(ocr_result["height"][i:j+1])
                positions.append((x, y, w, h))
                break
    return positions