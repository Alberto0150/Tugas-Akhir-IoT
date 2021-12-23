#define pinDigitalRelay 4
// gnd -> gnd 
// vcc -> vcc (negatif)
//5v / 3.3v -> pin (positif)

//pin led yang kakinya panjang yang positif
//pin led yg kakinya pendek yg negatif

//normally open (NO)[kanan kalau dari arah tulisan GND, IN1, IN2, IN3, IN4, VCC] ke positif / pin kaki panjang
//common (COM) [tengah] ke negatif / pin kaki pendek


void setup() {
  // put your setup code here, to run once:

  pinMode(pinDigitalRelay, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite(pinDigitalRelay, HIGH); 
  delay(1000); 
  
  digitalWrite(pinDigitalRelay, LOW); 
  delay(1000);
}
