import cv2
import numpy as np

# Load the image
img = cv2.imread("images/1_mupiirv.jpg")

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Add Poisson noise to the image
noisy_img = np.random.poisson(0.8 * gray_img)

# Convert the image back to BGR format
noisy_img = cv2.cvtColor(noisy_img.astype(np.uint8), cv2.COLOR_GRAY2BGR)


# Display the original and result images
cv2.imshow("before", img)
cv2.imshow("after", noisy_img)
cv2.waitKey(0)