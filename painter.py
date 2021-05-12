# painter.py
from PIL import Image, ImageFilter, ImageFont, ImageDraw
import os

def add_top(img,caption):
    caption = caption.upper()
    print("loading image")
    current = Image.open(img)
    ch = current.height
    difference = current.height
    cw = current.width
    ch *= 1.2
    ch = int(ch)
    difference = ch - difference
    print(Fore.RED + Style.BRIGHT + "making new image 💄" + Style.RESET_ALL)
    top = Image.new('RGBA', (cw,ch), 'white')
    top.paste(current, (0,difference))
    
    print("captioning")
    font_size = int(cw*0.085)
    font = ImageFont.truetype('static/fonts/impact.ttf', font_size)
    image_editable = ImageDraw.Draw(top)
    top.save(img, optimize=True)
    print("image created")


def collage():
    image_w, image_h = 2000,2000
    collage_s = 100
    layerW = Image.open("static/fisW.png")
    layerB = Image.open("static/fisB.png")
    new = Image.new(layerW.mode, (image_w,image_h))
    file_dict = {
        1: "haifa",
        2: "israel",
        3: "jerusalem",
        4: "tel_aviv",
        5: "zionism",
    }
    x,y = 0,0
    for directory in file_dict.values():
        try:
            os.remove(f"static/{directory}/.DS_Store")
        except Exception as e:
            print(e)
        for imageFile in os.listdir(f"static/{directory}")[:100]:
            # put the image
            img = Image.open(f'static/{directory}/{imageFile}')
            img = img.resize((collage_s,collage_s))
            new.paste(img, (x,y))
            if x >= image_w: 
                y += collage_s
                x = 0
            else: x += collage_s
    new = Image.blend(new, layerW, 0.20)
    new = Image.blend(new, layerB, 0.03)
    new.save("dab.png", optimize=True)

collage()
