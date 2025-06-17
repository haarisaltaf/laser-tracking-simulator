from PIL import Image, ImageDraw, ImageFilter # TODO: add PIL to requirments.txt
from random import randint

# globals
global IMAGE_SIZE
IMAGE_SIZE = (640,480)

global BASE_X
global BASE_Y
BASE_X = randint(0, 640)
BASE_Y = randint(0, 480)

# TODO: could add salt and pepper noise to add further noise?
def generateFrame(coords):
    # Generating new image with blurred background
    print(f"laser coords: {coords}")
    img = Image.effect_noise(size = IMAGE_SIZE, sigma = 50)

    # adding the "laser" (white dot)
    draw = ImageDraw.Draw(img)
    draw.circle(xy = coords, radius = 5, outline = "white", fill = "white", width = 1)

    # blurring final image to make it more relative to real cameras
    filtered = img.filter(ImageFilter.GaussianBlur(radius=1))

    return filtered

for i in range(30):
    # 1 second at 30fps = 30 frames

    # generateFrame((BASE_X+i, BASE_Y)).show("generatedImage.png") # show image in a browser
    # prints the current frame then the funtion will print the coords for the laser
    print(f"frame: {i}")
    # adds i*4 to x to increase the difference in distance moved per frame of the laser, (randint(-1,1) adds random up/ down jitter to laser)
    generateFrame((BASE_X+(i*4), BASE_Y+(randint(-1,1)))).save(f"frames/frame{i}.png") # save image in frames folder
