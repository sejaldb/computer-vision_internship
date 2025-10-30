from ultralytics import YOLO
# Load a pretrained YOLO model (.pt file)
model = YOLO("yolov8n.pt")
# Run object detection on a local image or video
results = model.predict(source="image.jpg", conf=0.25, imgsz=640)
#save the results to disk
results[0].save(filename="output.jpg")
