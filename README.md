# Automated Attendance System Using Facial Recognition

## Overview
The **Automated Attendance System** project aims to transition from a manual attendance system to an automated facial biometric attendance system. This project was initiated in response to a proposal from my college to enhance attendance tracking by integrating facial recognition with existing infrastructure.

## Objective
- Train a facial recognition model and integrate it with the college’s camera infrastructure.
- Ensure accurate and efficient attendance tracking through biometric facial recognition.

## Approach
- **Face Detection:** Used **YOLOv8** for detecting faces in real-time.
- **Face Recognition:** Implemented **FaceNet** for recognizing and matching faces from the captured images.
- **Training Accuracy:** Achieved a 92% accuracy on the validation set after training with a dataset of students' facial images, captured under different orientations.

## Challenges Encountered
- **Camera Infrastructure Integration:** Unable to integrate the system with the college's existing camera infrastructure due to challenges such as:
  - **Lighting Variations:** Different lighting conditions affecting recognition accuracy.
  - **Distance and Angle:** Difficulty in recognizing facial patterns due to the camera being mounted at a fixed distance and angle.
  
## Solution and Current Implementation
- **Alternative Solution:** Since integration with the college's camera system wasn't feasible at the time, I proposed a different approach:
  - **Handheld Biometric Devices:** The model was successfully integrated into handheld biometric devices, which are now in use within the campus for automated attendance tracking.

## Technologies Used
- **YOLOv8** (for face detection)
- **FaceNet** (for face recognition)
- **Python** (for model training and integration)

## How to Run the Project
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/automated-attendance-system.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Train the face recognition model:
    - Ensure you have the student facial image dataset available.
    - Run the training script for YOLOv8 and FaceNet integration.
4. For system integration:
    - Follow the instructions in the `integration.md` for deploying the model into handheld biometric devices.

## Contributions
Feel free to fork this project, submit issues, or propose improvements. This project was developed as a learning experience and remains an ongoing exploration into effective biometric systems.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For further information, feel free to reach out via email or GitHub issues.
