# object_detection.py
import cv2
import time
import os
from flask import Flask, Response, render_template_string
from ultralytics import YOLO
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# CONFIG
ALERT_EMAIL = "your_email@gmail.com"  # APNA EMAIL DALO
EMAIL_PASS = "your_app_password"      # 16-DIGIT PASSWORD (Google App Password)
SAVE_DIR = "detected_objects"
os.makedirs(SAVE_DIR, exist_ok=True)

# Load YOLO
model = YOLO("yolov8n.pt")

app = Flask(__name__)

# EMAIL ALERT
def send_email(image_path, objects):
    msg = MIMEMultipart()
    msg['From'] = ALERT_EMAIL
    msg['To'] = ALERT_EMAIL
    msg['Subject'] = f"DETECTED: {', '.join(objects)}"

    body = f"Objects: {', '.join(objects)}\nTime: {time.strftime('%H:%M:%S')}"
    msg.attach(MIMEText(body, 'plain'))

    with open(image_path, 'rb') as f:
        img = MIMEImage(f.read())
        img.add_header('Content-Disposition', f'attachment; filename={os.path.basename(image_path)}')
        msg.attach(img)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(ALERT_EMAIL, EMAIL_PASS)
        server.send_message(msg)
        server.quit()
        print("EMAIL SENT!")
    except Exception as e:
        print("Email failed:", e)

# VIDEO STREAM
def generate_frames():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("WEBCAM NOT FOUND!")
        return

    cap.set(3, 640); cap.set(4, 480)
    prev_objects = set()
    cooldown = 0

    while True:
        ret, frame = cap.read()
        if not ret: break

        results = model(frame, conf=0.4, verbose=False)[0]
        annotated = results.plot()

        current = {model.names[int(c)] for c in results.boxes.cls} if results.boxes.cls.numel() > 0 else set()

        if current and (current != prev_objects or cooldown == 0):
            ts = time.strftime("%Y%m%d-%H%M%S")
            path = os.path.join(SAVE_DIR, f"detected_{ts}.jpg")
            cv2.imwrite(path, annotated)
            print(f"DETECTED: {', '.join(current)} → {path}")
            send_email(path, list(current))
            prev_objects = current
            cooldown = 30

        if cooldown > 0:
            cooldown -= 1
            cv2.putText(annotated, "ALERT SENT!", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

        fps = 1000 / results.speed['inference']
        cv2.putText(annotated, f"FPS: {fps:.1f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

        ret, buffer = cv2.imencode('.jpg', annotated)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/')
def index():
    return render_template_string('''
    <html>
    <head><title>AI Object Detection</title>
    <style>
        body {font-family: Arial; text-align: center; background: #f0f0f0;}
        h1 {color: #1976d2;}
        img {border: 5px solid #333; border-radius: 15px;}
    </style>
    </head>
    <body>
        <h1>AI Object Detection</h1>
        <p>Detects: person, laptop, dog, etc.</p>
        <img src="/video_feed" width="720">
        <p><small>Samne object dikhao!</small></p>
    </body>
    </html>
    ''')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    print("AI Object Detection Shuru...")
    print("Browser mein kholo: http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)