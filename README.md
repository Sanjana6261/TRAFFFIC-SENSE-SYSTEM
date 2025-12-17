# 🚦 Traffic Sense System (Smart Surveillance Project)

An AI-powered **Smart Surveillance & Traffic Monitoring System** built using **Python, Computer Vision, and Deep Learning**. This project focuses on real-time video analysis to detect vehicles, people, and traffic patterns for enhanced road safety and intelligent monitoring.

---

## 📌 Project Overview

The **Traffic Sense System** is designed to analyze live camera feeds or recorded videos to:

* Monitor traffic conditions
* Detect objects such as vehicles and humans
* Capture unknown or suspicious activity
* Assist in intelligent surveillance and traffic management

This project demonstrates the practical use of **YOLO (You Only Look Once)** models and **OpenCV** for real-time detection and tracking.

---

## 🎯 Objectives

* To build a smart surveillance system using AI
* To perform real-time object and face detection
* To capture snapshots of unknown faces or events
* To enhance traffic monitoring using deep learning
* To provide a scalable base for smart city applications

---

## 🧠 Technologies Used

* **Programming Language:** Python
* **Computer Vision:** OpenCV
* **Deep Learning Model:** YOLOv8
* **Frameworks & Libraries:**

  * ultralytics
  * numpy
  * cv2
* **Frontend (Basic):** HTML (Flask template)
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
TRAFFFIC-SENSE-SYSTEM/
│
├── TRAFFIC SENSE SYSTEM.ipynb   # Main Jupyter Notebook
├── traffic_report.csv          # Generated traffic analysis report
├── final_road_heatmap.png      # Final road congestion heatmap
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
│
├── data/                       # Input videos / images (if any)
├── output/                     # Generated outputs
│   ├── heatmaps/
│   └── reports/
│
├── models/                     # ML / CV models (YOLO, etc.)
└── .gitignore                  # Ignored files
```

smart-surveillance-project-2/
│
├── app.py                 # Main application file
├── camera.py              # Camera handling and detection logic
├── requirements.txt       # Project dependencies
├── .gitignore             # Ignored files
│
├── templates/
│   └── index.html         # Web interface
│
├── known_faces/            # Known person images
├── snapshots/              # Captured unknown images
│
├── yolov8n.pt              # YOLO object detection model
├── yolov8n-face.pt         # YOLO face detection model

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Sanjana6261/TRAFFFIC-SENSE-SYSTEM.git
cd TRAFFFIC-SENSE-SYSTEM
````

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

---

## 🚀 Features

* ✅ Real-time video surveillance
* ✅ Face detection using YOLO
* ✅ Vehicle & object detection
* ✅ Automatic snapshot capture
* ✅ Modular and scalable code structure
* ✅ Easy to extend for smart city use-cases

---

## 📸 Output

* Live video feed with bounding boxes
* Automatic saving of unknown faces
* Real-time object detection results

---

## 🔮 Future Enhancements

* Traffic density analysis
* Vehicle counting & classification
* License plate recognition (ANPR)
* Cloud-based data storage
* Alert system using SMS/Email
* Dashboard with analytics

---

## 👩‍💻 Author

**Sanjana Kushwah**
B.Tech (IT) Student
AI | Machine Learning | Computer Vision Enthusiast

🔗 GitHub: [Sanjana6261](https://github.com/Sanjana6261)

---

## 📜 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this project for educational purposes.

---

⭐ *If you like this project, don’t forget to give it a star on GitHub!* ⭐
