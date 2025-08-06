import face_recognition
import numpy as np
from database.mongo_config import collection

def verify_employee(image_path):
    image = face_recognition.load_image_file(image_path)
    unknown_encodings = face_recognition.face_encodings(image)

    if not unknown_encodings:
        return "Face not detected", None

    unknown_encoding = unknown_encodings[0]

    for employee in collection.find():
        known_encoding = np.array(employee['face_encoding'])
        match = face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=0.5)

        if match[0]:
            return "Access Granted", employee['name']

    return "Access Denied", None
