import cv2


def main():
    # Start capturing video from the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply Canny edge detection
        edges = cv2.Canny(blur, 100, 200)

        # Apply threshold
        _, thresh = cv2.threshold(edges, 190, 255, cv2.THRESH_BINARY)

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Draw rectangles around the contours on the original frame
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the original frame with rectangles
        cv2.imshow("Webcam Stream with Rectangles", frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the VideoCapture object and close windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
