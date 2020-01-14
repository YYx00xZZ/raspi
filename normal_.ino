const int pinSwitch = 7;
const int pinBuzzer = 3;
const int pinLed = 8;
const int pinRelay = 10;

int dr;
String str;

int state; // was = 0;
int newState;

int i;

void setup() {
  Serial.begin(9600);

  pinMode(pinLed, OUTPUT);
  digitalWrite(pinLed, LOW);
  pinMode(pinBuzzer, OUTPUT);
  pinMode(pinSwitch, INPUT);
  pinMode(pinRelay, OUTPUT);
  digitalWrite(pinRelay, LOW);
  state = digitalRead(pinSwitch);

  Serial.println(state);

}

void loop() {
  if (Serial.available() > 0)
  {
    str = Serial.readStringUntil('\n');
    if (str == "L0")
    {
      digitalWrite(pinLed, LOW);
    }
    if (str == "L1")
    {
      digitalWrite(pinLed, HIGH);
    }
    if (str == "R0")
    {
      digitalWrite(pinRelay, LOW);
    }
    if (str == "R1")
    {
      digitalWrite(pinRelay, HIGH);
    }
  }
  newState = digitalRead(pinSwitch);

  if (state != newState) {
    state = newState;
    Serial.println(state);
  }

  //  if the door is opened,
  //  the buzzer will buzz 3 times and stop
  //                         until its   REopened

  if (state == 1) {
    if (i < 5) {
      for (i = 0; i < 5; ) {
        tone(pinBuzzer, 3200, 100);
        switch (i) {
          case 0:
            delay(350);
            break;
          case 1:
            delay(425);
            break;
          case 2:
            delay(575);
            break;
          case 3:
            delay(800);
            break;
          case 4:
            delay(1200);
            break;
        }
        i++;
      }
    }
  }
  else {
    i = 0;
  }
  //  delay(500);
}
