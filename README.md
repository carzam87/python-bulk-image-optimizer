# bulk-image-optimizer.py
This is a simple script that allow you to optimize/compress all your images at once.

Working on a Wordpress project, I needed to optimize all images inside the upload folder (over 500 images and placed on several folders) and I didn't want to pay for any plugins/services, so I decided to do it myself. 
I wrote this python script to compress all the files inside an "input" folder keeping the subfolders structure.
This script use Pil (or Pillow), a Python Imaging Library to compress the images.

## Installation

##### Dependencies
Install PIL or Pillow
```
    pip install Pillow
```

## Usage
1. Download the python script. 

2. Put all your images that to be compressed inside the "input" directory. All compressed images will be saved in the "output" directory.

3. Select quality level for output images

```
		 opt.save(out_path, optimize=True, quality=<your desired quality level>)
```
4. Run script
```
		python3 python-bulk-image-optimizer.py
```




