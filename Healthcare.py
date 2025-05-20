import cv2
import numpy as np
import mediapipe as mp

# Initialize MediaPipe Selfie Segmentation
mp_selfie_segmentation = mp.solutions.selfie_segmentation
segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

# Load images
person_img = cv2.imread('person.jpeg')       # Your person image
background_img = cv2.imread('background.jpeg')  # Your new background image

# Resize background to person image size
background_img = cv2.resize(background_img, (person_img.shape[1], person_img.shape[0]))

# Convert person image to RGB
rgb_person = cv2.cvtColor(person_img, cv2.COLOR_BGR2RGB)

# Get segmentation mask
results = segmentation.process(rgb_person)
mask = results.segmentation_mask

# Create condition mask
condition = np.stack((mask,) * 3, axis=-1) > 0.5

# Combine images based on mask
output = np.where(condition, person_img, background_img)

# Show the result
cv2.imshow('Background Replaced', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save output if you want
cv2.imwrite('output.jpg', output)
