import cv2
import numpy as np

# Minimum and maximum area thresholds for filtering
MIN_AREA = 100
MAX_AREA = 5000

# Start video capture
cap = cv2.VideoCapture(0)

# Create background subtractor
background_subtractor = cv2.createBackgroundSubtractorMOG2()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Apply background subtraction
    fg_mask = background_subtractor.apply(frame)

    # Apply thresholding to get binary image
    _, thresh = cv2.threshold(fg_mask, 50, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around moving objects
    for contour in contours:
        # Calculate area of contour
        area = cv2.contourArea(contour)
        if MIN_AREA < area < MAX_AREA:
            # Draw bounding box if area is within specified range
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)
    cv2.imshow('Foreground Mask', fg_mask)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
