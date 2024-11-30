from ultralytics import YOLO

model = YOLO('best.pt')  

results = model.predict('input_videos/sample.mp4', project="output_videos", name="sample")
print(results[0])
for box in results[0].boxes:
    print(box)