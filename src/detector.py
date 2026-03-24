from ultralytics import YOLO

model = None

def detect_persons(frame):
    global model
    if model is None:
        model = YOLO("yolov8m.pt")

    results = model.predict(frame, imgsz=640, conf=0.25, classes=[0], verbose=False)
    out = []
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            out.append(([x1, y1, x2 - x1, y2 - y1], float(box.conf[0]), "person"))
    return out