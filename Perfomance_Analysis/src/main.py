from ultralytics import YOLO
# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolo11n.pt")
# Train the model using the 'coco8.yaml' dataset for 'n' epochs
results = model.train(data="coco8.yaml", epochs=7)
# Evaluate the model's performance on the validation set
results = model.val()
# Export the model to ONNX format
success = model.export(format="onnx")
