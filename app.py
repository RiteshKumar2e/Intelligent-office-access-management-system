from flask import Flask, request, jsonify
from deepface import DeepFace
import os
import shutil
import uuid
import json

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
DB_FOLDER = 'face_db'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DB_FOLDER, exist_ok=True)

# ----------- Registration Route -----------
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    emp_id = request.form['emp_id']
    file = request.files['image']

    emp_dir = os.path.join(DB_FOLDER, f"{emp_id}_{name}")
    os.makedirs(emp_dir, exist_ok=True)

    # Save the image to the employee directory
    file_path = os.path.join(emp_dir, file.filename)
    file.save(file_path)

    return jsonify({'message': f'Employee {name} with ID {emp_id} registered successfully.'})


# ----------- Verification Route -----------
@app.route('/verify', methods=['POST'])
def verify():
    file = request.files['image']
    temp_file_path = os.path.join(UPLOAD_FOLDER, f'{uuid.uuid4().hex}_{file.filename}')
    file.save(temp_file_path)

    # Check against all registered employees
    matched = False
    matched_name = None

    for emp_folder in os.listdir(DB_FOLDER):
        emp_path = os.path.join(DB_FOLDER, emp_folder)
        for img in os.listdir(emp_path):
            db_img_path = os.path.join(emp_path, img)
            try:
                result = DeepFace.verify(temp_file_path, db_img_path, enforce_detection=False)
                if result['verified']:
                    matched = True
                    matched_name = emp_folder
                    break
            except Exception as e:
                continue
        if matched:
            break

    os.remove(temp_file_path)

    if matched:
        return jsonify({'message': 'Employee Verified ✅', 'employee': matched_name})
    else:
        return jsonify({'message': 'Verification Failed ❌', 'employee': None})


# ----------- Main Runner -----------
if __name__ == '__main__':
    app.run(debug=True)
