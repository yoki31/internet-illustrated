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
    new = Image.new("RGBA", (2000,2000))
    file_dict = {
        1: "haifa",
        2: "israel",
        3: "jerusalem",
        4: "star_of_david",
        5: "tel_aviv",
        6: "zionism"
    }
    line = 0
    for directory in file_dict.values():
        for imageFile in os.listdir(f"static/{directory}")[:30]:
            # put the image
            img = Image.open(f'static/{directory}/{imageFile}')
            img = img.resize((100,100))
            new.paste(img, (0,0))
            new.paste(img, (100,100))
    new.save("dab.png", optimize=True)

collage()