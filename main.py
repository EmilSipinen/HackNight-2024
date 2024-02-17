# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import numpy as np

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range of color to detect
    # Update these values based on the color of your glove or object
    lower_color = np.array([0, 48, 80], dtype="uint8")
    upper_color = np.array([20, 255, 255], dtype="uint8")

    # Create a mask for color detection and perform bitwise and
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Find contours in the mask
    contours, _ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Optional: Draw the contours on the original frame
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    # Display the resulting frame
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
