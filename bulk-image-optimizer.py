import os
import subprocess
from pathlib import Path
from PIL import Image

CONVERT_PNG_TO_JPG = False
TOTAL_ORIGINAL = 0
TOTAL_COMPRESSED = 0
TOTAL_GAIN = 0


def compress(location):
    for r, d, f in os.walk(location):
        for item in d:
            compress(location + os.sep + item)

        for image in f:
            path = location
            input_path = path + os.sep + image
            out_path = path.replace(r'input', r'output')
            if image.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                if os.path.isfile(input_path):
                    global TOTAL_GAIN
                    global TOTAL_ORIGINAL
                    global TOTAL_COMPRESSED
                    opt = None
                    try:
                        opt = Image.open(input_path)
                    except:
                        #do nothing just print the file skipping
                        print(f'skipping file cannot open: {input_path}')
                        continue
                        
                    original_size = os.stat(input_path).st_size / 1024 / 1024
                    TOTAL_ORIGINAL += original_size
                    print(input_path)
                    print("Original size: " + f'{original_size:,.2f}' + " megabytes")
                    Path(out_path).mkdir(parents=True, exist_ok=True)
                    out_path = out_path + os.sep + image
                    # Convert .pgn to .jpg
                    if CONVERT_PNG_TO_JPG and image.lower().endswith('.png'):
                        im = opt
                        rgb_im = im.convert('RGB')
                        out_path = out_path.replace(".png", ".jpg")
                        rgb_im.save(out_path)
                        opt = Image.open(out_path)
                    opt.save(out_path, optimize=True, quality=85)
                    opt = Image.open(out_path)
                    compressed_size = os.stat(out_path).st_size / 1024 / 1024
                    TOTAL_COMPRESSED += compressed_size
                    gain = original_size - compressed_size
                    TOTAL_GAIN += gain
                    print("Compressed size: " + f'{compressed_size:,.2f}' + " megabytes")
                    print("Gain : " + f'{gain:,.2f}' + " megabytes")
                    opt.close()
            else:
                if os.path.isfile(input_path):
                    print('File not image, copying instead: ' + input_path)
                    subprocess.call('cp ' + input_path + ' ' + out_path, shell=True)


if __name__ == '__main__':
    start_path = os.path.dirname(os.path.abspath(__file__)) + os.sep + r"input"
    
    # ask if .pgn images should automatically converted to .jpg
    CONVERT_PNG_TO_JPG = input('Would you like to convert .png images to .jpg? (y/n): ') == 'y'
    TOTAL_GAIN = 0
    compress(start_path)
    print("---------------------------------------------------------------------------------------------")
    print('-------------------------------------------SUMMARY-------------------------------------------')
    print(
        "Original: " + f'{TOTAL_ORIGINAL:,.2f}' + " megabytes || " + "New Size: " + f'{TOTAL_COMPRESSED:,.2f}' +
        " megabytes" + " || Gain: " + f'{TOTAL_GAIN:,.2f}' + " megabytes ~" + f'{(TOTAL_GAIN / TOTAL_ORIGINAL) * 100:,.2f}'
        + "% reduction")
