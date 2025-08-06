from ultralytics import YOLO
import cv2

def detect_tailgating(video_path):
    model = YOLO("yolov8n.pt")  # or yolov8s.pt, if needed
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, verbose=False)
        detections = results[0].boxes.cls.tolist()

        person_count = sum(1 for cls in detections if int(cls) == 0)  # '0' is class for person

        if person_count > 1:
            print(f"⚠️ Tailgating Detected! People in frame: {person_count}")
        else:
            print(f"✅ Normal Entry. People in frame: {person_count}")

        cv2.imshow("Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
