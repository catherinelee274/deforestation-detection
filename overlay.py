import cv2

mask = cv2.imread("thresh_image.jpg", -1)
src = cv2.imread("output2.tif" , -1)

# convert mask to gray and then threshold it to convert it to binary
gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)

# find contours of two major blobs present in the mask
im2,contours,hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# draw the found contours on to source image
for contour in contours:
    cv2.drawContours(src, contour, -1, (255,0,0), thickness = 1)

# split source to B,G,R channels
b,g,r = cv2.split(src)

# add a constant to R channel to highlight the selected area in reed
r = cv2.add(b, 30, dst = b, mask = binary, dtype = cv2.CV_8U)

# merge the channels back together
cv2.merge((b,g,r), src)

cv2.imshow("final overlay", src) 

