import cv2                          # OpenCV: video capture and exhibition
import face_recognition             # Used to recognize stored faces
import numpy as np                  # Used to calculate the probable person
import os                           # Used to manipulate files
from datetime import datetime       # Used to store the exact time when the student entered in the class


video_capture = cv2.VideoCapture(0)
students_data = {
    550788: {"name": "Gabriel Diegues", "presence_time_s": 0, "present": False},
    99367: {"name": "Luiza Cristina", "presence_time_s": 0, "present": False},
    551180: {"name": "Pedro Palladino", "presence_time_s": 0, "present": False},
    99242: {"name": "Renato Izumi", "presence_time_s": 0, "present": False}
    }
known_faces_encodings = []
known_faces_names = []
face_folder = "Faces"
for file_name in os.listdir(face_folder):
    face_image_path = os.path.join(face_folder, file_name) # Getting each image path. Example: Faces\550788.jpeg
    face_image = face_recognition.load_image_file(face_image_path) # Transforming the image into an array
    face_encoding = face_recognition.face_encodings(face_image)[0] # Creating a fingerprint for the first face that appears in the image based on the image's array
    known_faces_encodings.append(face_encoding) # Addinng the fingerprint into the array that stores all known fingerprints
    student_rm = int(file_name.split('.')[0]) # Extracting the student's RM
    if student_rm in students_data.keys():
        known_faces_names.append(student_rm) # Adding the rm of each student
    
total_class_time = 0

while video_capture.isOpened():
    ret, frame = video_capture.read()
    if not ret:
        # video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)  # returns to the beggining of the video
        # continue
        print("End of video or loading error")
        break
    
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (500, 500)) # Redimensioning the video to 500X500

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Converting video color to RGB

    faces_locations_video = face_recognition.face_locations(rgb_frame) # Locates the faces found on the video
    if faces_locations_video:
        faces_encodings_video = face_recognition.face_encodings(rgb_frame, faces_locations_video) # Creates fingerprints for faces found on the video
        for (top, right, bottom, left), face_encoding in zip(faces_locations_video, faces_encodings_video):
            matches = face_recognition.compare_faces(known_faces_encodings, face_encoding) # A list of True/False values indicating which known_face_encodings match the face encoding 
            personName = "unkown" 
            # Calculates the most probable person
            face_distance = face_recognition.face_distance(known_faces_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]: # If the face is recognized
                personData = students_data[known_faces_names[best_match_index]]
                personName = personData["name"]
                personData["presence_time_s"] += 1
            
            # Drawing a square around the face and display the person's name below the square 
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, personName, (left + 6, bottom - 6), font, 0.5, (0, 0, 0), 1)

    cv2.imshow("Video", frame)
    total_class_time += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

for rm in students_data.keys():
    current_student = students_data[rm]
    presence_time = current_student["presence_time_s"]
    presence_ratio = presence_time / total_class_time
    if presence_ratio >= 0.8:
        current_student["present"] = True
    
    print(f"RM: {rm} | Name: {current_student["name"]} | Present:{"Yes" if current_student["present"] else "No"} | Presence time: {current_student["presence_time_s"]} | Class time: {total_class_time}")
