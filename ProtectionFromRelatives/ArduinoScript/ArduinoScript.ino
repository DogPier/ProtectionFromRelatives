#define IK 3

void setup() {
  Serial.begin(9600);
  pinMode(IK, INPUT);
}

void loop() {
  int s = digitalRead(IK);
  if (s == 1) {
    Serial.println(0);
  }
  else {
    Serial.println(1);
  }
  delay(50);
}
