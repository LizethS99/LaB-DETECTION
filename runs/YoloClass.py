from ultralytics import YOLO

"""if __name__ == '__main__':
    model = YOLO('yolov8n-seg.yaml')
    model = YOLO('yolov8n-seg.pt')
    model = YOLO('yolov8n-seg.yaml').load('yolov8n.pt')

    result = model.train(data='./Data/dataset.yaml', epochs=40, imgsz=640, batch=2)"""

if __name__ == '__main__':
    model = YOLO('yolov8n-cls.yaml')
    model = YOLO('yolov8n-cls.pt')
    model = YOLO('yolov8n-cls.yaml').load('yolov8n-cls.pt')

    result = model.train(data='./DataV2/Classify', epochs=80, imgsz=640, batch=2)
