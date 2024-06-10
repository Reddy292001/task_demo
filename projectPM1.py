import cv2

# Load the pre-trained LPR model
lpr_model = cv2.CascadeClassifier('lpr_model.xml')  # You need to train or obtain a pre-trained model for license plate detection

# Provide the path to the image file containing the vehicle
image_path = '"C:\\Users\\singa\\Downloads\\AP_Number.jpg"'  # Replace 'path_to_your_image.jpg' with the actual path to your image file

# Load the image from the specified file
image = cv2.imread(image_path)

# Convert the image to grayscale
white_image = cv2.cvtColor(image, cv2.COLOR_BGR2white)

# Detect license plates in the image
plates = lpr_model.detectMultiScale(white_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Loop over the detected plates and draw bounding boxes
for (x, y, w, h) in plates:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 2)

# Display the image with bounding boxes
cv2.imshow('License Plate Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
