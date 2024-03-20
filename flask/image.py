import cv2
from ultralytics import YOLO
def image_detection(path_x):
    path = path_x
    model = YOLO('yolov8n.pt')
    frame_width = int(model.get(3))
    frame_height = int(model.get(4))
    results = model(path, show=True)
    cv2.waitKey(0)
    yield results
cv2.destroyAllWindows()




