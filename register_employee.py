import face_recognition
import cv2
import numpy as np
from database.mongo_config import collection

def register_employee(name, emp_id, image_path):
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)

    if len(encodings) == 0:
        return "Face not detected."

    employee_data = {
        "emp_id": emp_id,
        "name": name,
        "face_encoding": encodings[0].tolist()
    }

    collection.insert_one(employee_data)
    return "Employee registered successfully."
