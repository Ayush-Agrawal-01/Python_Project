#help from:- https://pythonexamples.org/python-opencv-cv2-resize-image/
import cv2
# cv2 can convert jpg to png.

# configurable parameters
source = "ROG Strix 2019_1920x1080.png"
destination = "New_image.jpg"
# percent by which the image is resized
scale_percent = 50

src = cv2.imread(source)


# calculate the 50 percent of original dimensions
New_width = int(src.shape[1] * scale_percent / 100)
New_height = int(src.shape[0] * scale_percent / 100)

# resize image
output = cv2.resize(src, (New_width, New_height))

cv2.imwrite(destination, output)
# cv2.waitKey(0)