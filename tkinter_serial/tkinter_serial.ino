int incomingData;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  Serial.write("Press the button to control LED (Message from Arduino");
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available()) {
    incomingData = Serial.read();
    if (incomingData == '1') {
      digitalWrite (LED_BUILTIN, HIGH);
      Serial.write("LED TURNED ON");
    }
    if (incomingData == '0') {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.write("LED TURNED OFF");
    }
  }
}
