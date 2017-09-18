import cv2
import sys

# get user supplied values
imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

# create haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,  # adjust here is catching spurious results
    minNeighbors=5,
    minSize=(30, 30),
    # flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# draw rectangle around faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
