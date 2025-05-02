from ultralytics import YOLO
# Load a pretrained YOLO11 segment model
model1 = YOLO("yolo11n-seg.pt")
model2 = YOLO("yolo11n-seg.pt")

# Train the model
results1 = model1.train(data=r"C:\Users\bayka\Documents\AAU Robot\8sem\MachineVision\AMV_Exam\Miniprojekt.v2-polygon-screw-detection.yolov11\data.yaml", epochs=100, imgsz=640, plots=True, seed=42, save_period=5, project=r"C:\Users\bayka\Documents\AAU Robot\8sem\MachineVision\AMV_Exam\Model_poly", name="Poly_run1", patience=10, cache=True, device="cpu")
results2 = model2.train(data=r"C:\Users\bayka\Documents\AAU Robot\8sem\MachineVision\AMV_Exam\Screw Detection.v1-bounding-box-screw-detection.yolov11\data.yaml", epochs=100, imgsz=640, plots=True, seed=42, save_period=5, project=r"C:\Users\bayka\Documents\AAU Robot\8sem\MachineVision\AMV_Exam\Model_Bounding", name="Box_run1", patience=10, cache=True, device="cpu")