#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <SmtpClient.h>

#define flameSensorPin A0
#define SENDER_EMAIL "sender@example.com"
#define SENDER_PASSWORD "senderPassword"
#define RECIPIENT_EMAIL "recipient@example.com"
#define WIFI_SSID "YourWiFiSSID"
#define WIFI_PASSWORD "YourWiFiPassword"

int flameSensorValue;
WiFiClientSecure client;
SmtpClient smtp(client);

void setup() {
  Serial.begin(115200);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  flameSensorValue = analogRead(flameSensorPin);
  if (flameSensorValue > 800) {
    if (smtp.send("smtp.example.com", 465, SENDER_EMAIL, RECIPIENT_EMAIL,
                  "Fire detected!", "There is a fire!")) {
      Serial.println("Email sent successfully");
    } else {
      Serial.println("Email sending failed");
    }
  }
  delay(1000);
}
