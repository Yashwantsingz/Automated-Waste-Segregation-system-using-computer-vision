Automated Waste Segregation System using YOLO


Project Goal
The goal of this project is to develop an automated system capable of identifying and segregating different types of waste materials using computer vision and machine learning. This aims to improve recycling efficiency, reduce landfill waste, and contribute to a more sustainable environment.

Current Status: Model Training Successful!
We are excited to announce that we have successfully trained our YOLO (You Only Look Once) object detection model for waste segregation.

The model has been trained on a custom dataset to recognize the following classes of waste:
1.Cardboard
2.Glass
3.Metal
4.Paper
5.Plastic

Through rigorous testing on our validation data, the trained model is demonstrating promising performance in accurately identifying and localizing these different waste categories in images and video streams. The core computer vision capability for waste detection is now functional.

Next Steps: Building the Frontend UI
With the object detection model successfully trained and performing well, the next major phase of this project is to develop the frontend user interface (UI).

This frontend will be responsible for:
Displaying the real-time video feed from a camera.
Overlaying the detection results (bounding boxes and class labels) from the YOLO model.
Potentially providing a dashboard to visualize sorting statistics.

(Future) Integrating with hardware control to trigger the physical segregation mechanism based on the model's output.

We will be focusing our efforts on building a user-friendly and intuitive interface to showcase the capabilities of the trained model in a practical application scenario.
