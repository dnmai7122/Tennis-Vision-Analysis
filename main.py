from ultralytics import YOLO

model = YOLO('yolov8x')
res = model.predict('input/tennis-play.mp4', save=True)
print(res)
print("boxes")
for box in res[0].boxes:
    print(box)