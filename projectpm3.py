import cv2
import numpy as np

# Load the image
image = cv2.imread('C:\\Users\\singa\\Downloads\\AP_Number.jpg')

# Create a white image of the same size and type as the original image
white_image = np.ones_like(image) * 255

# Display the white image
cv2.imshow('White Image', white_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
