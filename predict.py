from ultralytics import YOLOv10

model = YOLOv10("best.pt")
#model.predict(source="picture",imgsz=640,device=0,conf=0.60,save=True)
model.predict(source="D:/Software/Pycharm/yolov10-main/data/NEU-DET/test/images",imgsz=640,device=0,conf=0.05,save=True)
pass