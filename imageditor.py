
from PIL import Image, ImageEnhance, ImageFilter
import os

# Correct input and output directories
input_path = r'C:\Users\c3175\OneDrive\Python Project\Image Editor project\imagedit_input.py'
output_path = r'C:\Users\c3175\OneDrive\Python Project\Image Editor project\imagedit_output.py'

# Create the output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

# Iterate over all files in the input directory
for filename in os.listdir(input_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Construct the full file path
        img_path = os.path.join(input_path, filename)
        
        # Open the image
        img = Image.open(img_path)
        
        # Apply sharpen filter and convert to grayscale
        edit = img.filter(ImageFilter.SHARPEN).convert('L')
        
        # Enhance the contrast
        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)
        
        # Construct the output file path
        output_filename = os.path.splitext(filename)[0] + '_edited.jpg'
        output_img_path = os.path.join(output_path, output_filename)
        
        # Save the edited image
        edit.save(output_img_path)
