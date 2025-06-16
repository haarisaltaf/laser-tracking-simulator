from PIL import Image, ImageDraw, ImageFilter
from random import randint
from time import sleep

# globals
global IMAGE_SIZE
IMAGE_SIZE = (640,480)

global BASE_X
global BASE_Y
BASE_X = randint(0, 630)
BASE_Y = randint(0, 470)

def generateFrame(coords):
    # Generating new image
    img = Image.new(mode="RGB", size=IMAGE_SIZE, color = "black")

    # adding the "laser" (white dot)
    draw = ImageDraw.Draw(img)
    draw.circle(xy = coords, radius = 5, outline = "white", fill = "white", width = 2)

    # blurring final image to make it more relative to real cameras
    filtered = img.filter(ImageFilter.GaussianBlur(radius=1))

    return filtered


for i in range(5):
    # assuming 5 frames generated, 4 pixels apart at each image taken
    # generateFrame((BASE_X+i, BASE_Y)).show("generatedImage.png")
    generateFrame((BASE_X+(i*4), BASE_Y)).save(f"frames/frame{i}.png")
