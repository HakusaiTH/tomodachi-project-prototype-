#include <FirebaseESP8266.h>
#if defined(ESP32)
#include <WiFi.h>
#elif defined(ESP8266)
#include <ESP8266WiFi.h>
#endif

#define WIFI_SSID "FF1_15" // your wifi SSID
#define WIFI_PASSWORD "123456789" //your wifi PASSWORD

#define FIREBASE_HOST "https://ai-chan-3074e-default-rtdb.asia-southeast1.firebasedatabase.app/" // change here
#define FIREBASE_AUTH "6ZvQouJvYS9gnYN9deaY3PPyLgu0Xa78mtQTf6vD"  // your private key
FirebaseData firebaseData;

int LedPin = D0;
void setup ()
{
  pinMode(LedPin, OUTPUT);
  digitalWrite(LedPin,LOW);
  
  Serial.begin(9600);
  // connect to wifi.
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("connected: ") ;
  Serial.println(WiFi.localIP());
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);     
}
void loop ()
{
  if(Firebase.getString(firebaseData, "/iot_1"))
  {
    String ledstatus = firebaseData.stringData();
    if(ledstatus.toInt() == 1){
      digitalWrite(LedPin, LOW);
      Serial.println("on");
    }
    else {
      digitalWrite(LedPin, HIGH);
      Serial.println("off");
    }
  }else{
    Serial.print("Error in getInt, ");
    Serial.println(firebaseData.errorReason());
  } 
}
