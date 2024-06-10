import cv2

# Function to deduct money based on license plate
def deduct_money(plate_number):
    # Simplified logic: deduct fixed amount for each plate
    # You would replace this with your actual deduction logic
    amount_deducted = 50  # Example: deduct $50 for each plate
    print(f"Money deducted for plate {plate_number}: ${amount_deducted}")

# Load the pre-trained LPR model
lpr_model = cv2.CascadeClassifier('lpr_model.xml')  # You need to train or obtain a pre-trained model for license plate detection
# Provide the path to the image file containing the vehicle
image_path = '"C:\\Users\\singa\\Downloads\\AP_Number.jpg"'  # Replace 'path_to_your_image.jpg' with the actual path to your image file

image = cv2.imread('image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect license plates in the image
plates = lpr_model.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Loop over the detected plates and draw bounding boxes
for (x, y, w, h) in plates:
    # Extract license plate region
    plate_roi = gray_image[y:y+h, x:x+w]
    
    # Perform license plate recognition (not implemented in this example)
    plate_number = "ABC123"  # Example: hard-coded plate number
    
    # Deduct money based on the recognized plate number
    deduct_money('AP 1 A 1234')

    # Draw bounding box around the detected plate
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the image with bounding boxes
cv2.imshow('License Plate Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
