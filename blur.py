# import the necessary packages
import cv2

def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

# construct the argument parse and parse the arguments
threshold = 100.0

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = cv2.VideoCapture(0)  # Change 0 to the index of the webcam if you have multiple cameras

# loop over frames from the video stream
while True:
    # grab the frame from the video stream
    ret, frame = vs.read()

    # convert the frame to grayscale and compute the focus measure
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    text = "Not Blurry"

    # if the focus measure is less than the supplied threshold,
    # then the image should be considered "blurry"
    if fm < threshold:
        text = "Blurry"

    # display the frame with the text
    cv2.putText(frame, "{}: {:.2f}".format(text, fm), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("Frame", frame)

    # if the `q` key was pressed, break from the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cleanup
vs.release()
cv2.destroyAllWindows()
