from cv2 import imread, imshow, waitKey, destroyAllWindows, threshold, THRESH_BINARY, SimpleBlobDetector_create, SimpleBlobDetector_Params, DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, drawKeypoints
from numpy import array


# constants
global PATH_TO_FRAMES
PATH_TO_FRAMES = "../simulator/frames"

# TODO: grab the number of frames in the directory; currently assuming 30 frames
global DEFAULT_NUMBER_OF_FRAMES
DEFAULT_NUMBER_OF_FRAMES = 30


def grabBlobKeypoint():
    # grab frame in grayscale mode
    currentFrame = imread(PATH_TO_FRAMES+"/frame0.png", 0)
    imshow("frame0", currentFrame)
    # waits till user presses any key to stop python kernel crashing
    waitKey(0)
    # destroys open windows after key press
    destroyAllWindows()

    # # making only the pixels above 200 brightness visible, the rest are black.
    # thresholdValue, thresholdFrame = threshold(currentFrame, 200, 255, THRESH_BINARY)

    # Setting the parameters for the simple blob detector
    params = SimpleBlobDetector_Params()
    params.minThreshold = 190
    params.maxThreshold = 255

    params.filterByCircularity = True

    params.blobColor = 255
    # params.minArea = 5

    params.filterByCircularity = True
    params.minCircularity = 0.5

    # Creating the blob detector using the parameters set
    detector = SimpleBlobDetector_create(params)
    blobsDetected = detector.detect(currentFrame)
    print(blobsDetected)

    output = drawKeypoints(currentFrame, blobsDetected, array([]), (0, 0, 255),
                               DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
     
    # Show the output
    imshow("Blobs Detected", output)
    waitKey(0)
    destroyAllWindows()


grabBlobKeypoint()

# simulating the fast steering mirror
def fastSteeringMirror():
    pass
