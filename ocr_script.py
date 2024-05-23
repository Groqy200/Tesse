import pytesseract
from pytesseract import Output
import cv2
import os
import pandas as pd

def ocr_to_csv(input_path, output_path):
    # Load the image from the input path
    image = cv2.imread(input_path)

    # Perform OCR using pytesseract
    data = pytesseract.image_to_data(image, output_type=Output.DICT)

    # Convert OCR data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    csv_filename = os.path.join(output_path, os.path.basename(input_path).replace('.png', '.csv'))
    df.to_csv(csv_filename, index=False)

# Example usage
if __name__ == "__main__":
    input_folder = 'input'
    output_folder = 'output'
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):  # assuming your input files are PNGs
            input_file = os.path.join(input_folder, filename)
            ocr_to_csv(input_file, output_folder)
