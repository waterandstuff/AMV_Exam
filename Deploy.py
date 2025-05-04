from ultralytics import YOLO


model = YOLO(r"C:\Users\bayka\Documents\AAU Robot\AppliedMachineVision\AMV_Exam\Model_Bounding\Box_run13\weights\best.pt")
#model = YOLO(r"C:\Users\bayka\Documents\AAU Robot\AppliedMachineVision\AMV_Exam\Model_poly\Poly_run12\weights\best.pt")

model.predict(source=r"C:\Users\bayka\Documents\AAU Robot\AppliedMachineVision\AMV_Exam\Screw Detection.v1-bounding-box-screw-detection.yolov11\test\images", show=True, save=True, conf=0.7, iou=0.5, save_txt=True, save_conf=True, project=r"C:\Users\bayka\Documents\AAU Robot\AppliedMachineVision\AMV_Exam\Screw Detection.v1-bounding-box-screw-detection.yolov11\test", name="Box_run12") 