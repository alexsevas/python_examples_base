# conda activate allpy310
# Add watermark to pictures in folder with PIL

import os
from PIL import Image

def watermark_photo(input_image_path,watermark_image_path,output_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path).convert("RGBA")
    position = base_image.size
    newsize = (int(position[0]*8/100),int(position[0]*8/100))
    watermark = watermark.resize(newsize)
    new_position = position[0]-newsize[0]-20,position[1]-newsize[1]-20
    transparent = Image.new(mode='RGBA',size=position,color=(0,0,0,0))
    transparent.paste(base_image,(0,0))
    transparent.paste(watermark,new_position,watermark)
    image_mode = base_image.mode
    print(image_mode)
    if image_mode == 'RGB':
        transparent = transparent.convert(image_mode)
    else:
        transparent = transparent.convert('P')
    transparent.save(output_image_path,optimize=True,quality=100)
    print("Saving"+output_image_path+"...")

folder = input("Enter Folder Path:") # C:\PROJECTS\_DATA_\images_with_bg
watermark = input("Enter Watermark Path:") # C:\PROJECTS\_DATA_\image.jpg
os.chdir(folder)
files = os.listdir(os.getcwd())
print(files)

if not os.path.isdir("output"):
    os.mkdir("output")

c = 1
for f in files:
    if os.path.isfile(os.path.abspath(f)):
        if f.endswith(".png") or f.endswith(".jpg"):
            watermark_photo(f,watermark,"output/"+f)
