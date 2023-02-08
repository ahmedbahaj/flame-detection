import RPi.GPIO as GPIO
import time
import smtplib

# The script sets up the flame sensor on pin 21 (change this to the correct pin number for your setup) and waits for the sensor to detect a fire. 
# When a fire is detected, the send_email function is called to send an email with the subject "Fire Alert!" and the message "A fire has been detected."
FLAME_SENSOR_PIN = 21  # change this to the pin number your flame sensor is connected to

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME_SENSOR_PIN, GPIO.IN)

def send_email(subject, message):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "your_email@gmail.com"
    smtp_password = "your_email_password"
    recipient = "recipient_email@example.com"

    message = f"Subject: {subject}\n\n{message}"

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(smtp_username, smtp_password)
            smtp.sendmail(smtp_username, recipient, message)
            print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

def detect_fire():
    while True:
        if GPIO.input(FLAME_SENSOR_PIN) == 1:
            print("Fire detected")
            send_email("Fire Alert!", "A fire has been detected.")
            break
        time.sleep(1)

if __name__ == "__main__":
    detect_fire()
