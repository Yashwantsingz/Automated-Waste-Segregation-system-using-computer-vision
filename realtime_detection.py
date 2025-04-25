from ultralytics import YOLO
import cv2

# Load your pre-trained YOLO model
model = YOLO(r"D:\archive\my_model\my_model.pt") # Replace with the actual path to your model file

# Open a connection to your webcam (usually 0)
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection on the frame
    results = model(frame)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the frame with detections
    cv2.imshow("YOLOv8 Detection", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()