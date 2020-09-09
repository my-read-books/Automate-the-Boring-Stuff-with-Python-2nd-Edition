import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILE_NAME = "../automate_online-materials/catlogo.png"

logoIm = Image.open(LOGO_FILE_NAME)
logoIm = logoIm.resize((SQUARE_FIT_SIZE // 4, SQUARE_FIT_SIZE // 4))
logoWidth, logoHeight = logoIm.size

os.makedirs("withLogo", exist_ok=True)

for filename in os.listdir("."):
    if not (filename.endswith(".png") or filename.endswith(".jpg")):
        continue
    im = Image.open(filename)
    width, height = im.size

    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        print("Change image size " + filename)
        im = im.resize((width, height))

    print("Add logo to image" + filename)
    im.paste(logoIm, (width-logoWidth, height - logoHeight), logoIm)
    im.save(os.path.join("withLogo", filename))

