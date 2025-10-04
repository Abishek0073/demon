import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import smtplib
from email.mime.text import MIMEText
import cv2
import joblib

# Email setup (use environment variables or another secure method for credentials)
def send_alert_notification(subject, message, recipient_email):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    sender_email = os.getenv("SENDER_EMAIL")  # Set environment variables for security
    sender_password = "your-app-generated-password"
    server.login(sender_email, sender_password)

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

# Theft detection function
def detect_shop_theft(frame, model):
    # Preprocess the frame for prediction
    frame_resized = cv2.resize(frame, (224, 224))
    frame_normalized = frame_resized / 255.0
    frame_flattened = frame_normalized.flatten().reshape(1, -1)  # Flatten for prediction

    # Make prediction
    y_pred = model.predict(frame_flattened)
    if y_pred[0] == 1:
        return True  # Theft detected
    return False  # No theft detected

# Load your trained model here
# model = RandomForestClassifier()  # Example placeholder for model loading

# Example usage
# frame = cv2.imread('path_to_image.jpg')  # Replace with actual frame capture
# if detect_shop_theft(frame, model):
#     send_alert_notification("Theft Alert", "Theft has been detected in the store!", "recipient@example.com")

def train_and_save_model(X_train, y_train, model_path):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)  # Save the trained model
    return model

if __name__ == "__main__":
    # Load your data
    # X, y = ...

    # Split the data
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train and save the model
    model_path = "theft_detection_model.pkl"
    model = train_and_save_model(X_train, y_train, model_path)

    # Load the model
    # loaded_model = joblib.load(model_path)
