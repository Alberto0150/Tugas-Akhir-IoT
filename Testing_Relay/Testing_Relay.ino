//Basic 
//pin led yang kakinya panjang yang positif
//pin led yg kakinya pendek yg negatif

//normally open (NO)[kanan kalau dari arah tulisan GND, IN1, IN2, IN3, IN4, VCC] ke pin positif elektronik (dia penerus power dari COM)
//common (COM) [tengah] dari power source

// GND -> negatif
// Pin -> positif 
// 5v,3v -> power (ardu -> vcc)

//Referensi : https://www.nyebarilmu.com/cara-mengakses-relay-menggunakan-arduino-uno/
// ardu   - board  - relay 
// pinDig - ...    - InX
// GND    - GND    - GND,COM
// 5v     - ledPos - NO
// ...    - ledNeg - VCC


#define pinDigitalRelay1 4
#define pinDigitalRelay2 2
void setup() {
  // put your setup code here, to run once:

  pinMode(pinDigitalRelay1, OUTPUT);
  pinMode(pinDigitalRelay2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite(pinDigitalRelay1, HIGH); 
  digitalWrite(pinDigitalRelay2, LOW); 
  delay(1000); 
  
  digitalWrite(pinDigitalRelay1, LOW); 
  digitalWrite(pinDigitalRelay2, HIGH); 
  delay(1000);
}
