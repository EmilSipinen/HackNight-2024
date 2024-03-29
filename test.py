import cv2
import numpy as np

# Minimum and maximum area thresholds for filtering
MIN_AREA = 100
MAX_AREA = 1000

blue = 190
green = 191
red = 184
filter = 50


def color(input):
    if input >= 255:
        return 255
    elif input <= 0:
        return 0
    else:
        return input


# Define the color range for filtering
lower_color = np.array(
    [color(blue - filter), color(green - filter), color(red - filter)]
)
upper_color = np.array(
    [color(blue + filter), color(green + filter), color(red + filter)]
)

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
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around moving objects
    for contour in contours:
        # Calculate area of contour
        area = cv2.contourArea(contour)
        if MIN_AREA < area < MAX_AREA:
            # Filter contours based on color
            mask = np.zeros(frame.shape[:2], dtype="uint8")
            cv2.drawContours(mask, [contour], -1, 255, -1)
            mean_color = cv2.mean(frame, mask=mask)[:3]

            if all(lower_color <= mean_color) and all(mean_color <= upper_color):
                # Draw bounding box if area is within specified range and color matches
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("Frame", frame)
    cv2.imshow("Foreground Mask", fg_mask)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
