# pip install cmake
# pip install face_recognition
# pip install opencv-python
# pip install numpy
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import pyttsx3

# Load known faces
ashwin_image = face_recognition.load_image_file("faces/ashwin.jpg")
ashwin_encoding = face_recognition.face_encodings(ashwin_image)[0]

rishi_image = face_recognition.load_image_file("faces/rishi.jpg")
rishi_encoding = face_recognition.face_encodings(rishi_image)[0]

known_face_encodings = [ashwin_encoding, rishi_encoding]
known_face_names = ["Ashwin", "Rishi"]

# List of expected students
students = known_face_names.copy()

# Initialize video capture from webcam
video_capture = cv2.VideoCapture(0)

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Open CSV file for writing attendance
csv_filename = f"{current_date}.csv"
with open(csv_filename, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)

    # Initialize font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Initialize the speech engine
    engine = pyttsx3.init()

    while True:
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Recognize faces
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            if len(face_encoding) > 0:  # Ensure there's at least one face encoding
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distance)

                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                    # Add the text if a person is present
                    if name in known_face_names:
                        bottomLeftCornerOfText = (10, 50)
                        fontScale = 1
                        FontColor = (255, 255, 255)
                        thickness = 2
                        lineType = 2
                        cv2.putText(frame, f"{name} present", bottomLeftCornerOfText, font, fontScale, FontColor, thickness, lineType)
                        if name in students:
                            students.remove(name)
                            current_time = datetime.now().strftime("%H:%M:%S")
                            csv_writer.writerow([name, current_time])
                            engine.say("Thank you")
                            engine.runAndWait()
                else:
                    engine.say("Please try again")
                    engine.runAndWait()

        cv2.imshow("Attendance", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Release video capture and close windows
video_capture.release()
cv2.destroyAllWindows()