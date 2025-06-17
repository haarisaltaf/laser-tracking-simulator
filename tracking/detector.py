from cv2 import imread, imshow, waitKey, destroyAllWindows, threshold, THRESH_BINARY, SimpleBlobDetector

# constants
global PATH_TO_FRAMES
PATH_TO_FRAMES = "../simulator/frames"

# TODO: grab the number of frames in the directory; currently assuming 30 frames
global DEFAULT_NUMBER_OF_FRAMES
DEFAULT_NUMBER_OF_FRAMES = 30

# grab frame in grayscale mode
currentFrame = imread(PATH_TO_FRAMES+"/frame0.png", 0)
imshow("frame0", currentFrame)
# waits till user presses any key to stop python kernel crashing
waitKey(0)
# destroys open windows after key press
destroyAllWindows()

# making only the pixels above 200 brightness visible, the rest are black.
thresholdValue, thresholdFrame = threshold(currentFrame, 200, 255, THRESH_BINARY)
imshow("threshFrame0", thresholdFrame)
# waits till user presses any key to stop python kernel crashing
waitKey(0)
# destroys open windows after key press
destroyAllWindows()

detector = SimpleBlobDetector()
blobsDetected = detector.detect(thresholdFrame)
print(blobsDetected)
