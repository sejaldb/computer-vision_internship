from ultralytics import YOLO
# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolo11m.pt")
#object detection
yolo predict model=yolo11l.pt source="" imgsz=640 conf=0.25
#object segmentation
yolo predict task=segment model=yolov8s-seg.onnx source=""
# Train the model using the '.yaml' dataset for 3 epochs
results = model.train(data="coco8.yaml", epochs=3)
