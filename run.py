# entry point to run entire laser sim

import matplotlib.pyplot as plt
import simulator.frame_generator as frame_generator
import tracking.detector as detector
import tracking.tracker as tracker
from PIL import Image, ImageDraw


frame_generator.generateFrames()
for currentFrameNumber in range(30):
    # currentFrameCoords = detector.grabBlobKeypoint(currentFrameNumber)
    print(currentFrameNumber)
    laserXCoords, laserYCoords =  detector.grabBlobKeypoint(currentFrameNumber)[0].pt[0], detector.grabBlobKeypoint(currentFrameNumber)[0].pt[1]
    errorData, x, y = tracker.applyPID(laserXCoords, laserYCoords)
    
    # saving the tracking error over time
    plt.plot(errorData)
    plt.title("Tracking Error Over Time")
    plt.xlabel("Frame")
    plt.ylabel("Distance from Center (px)")
    plt.grid(True)
    plt.savefig(f"outputs/trackingError/frame{currentFrameNumber}Error.png") 

    # draw final image based on the correct x and y values, simulating what would be seen on fsm
    final_image = Image.new("L", (640,480), 0)  # 0 = black
    draw = ImageDraw.Draw(final_image)
    dot_radius = 4
    # Define the bounding box for the white dot
    top_left = (int(x) - dot_radius, int(y) - dot_radius)
    bottom_right = (int(x) + dot_radius, int(y) + dot_radius)
    # Draw the white laser dot
    draw.ellipse([top_left, bottom_right], fill=255)
    final_image.save(f"outputs/finalImages/frame{currentFrameNumber}Final.png") 
