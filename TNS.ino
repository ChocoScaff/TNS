const int microphonePin = A0;
int ledPin = 10;

void setup() {
  Serial.begin(9600);
  //Serial.println("Hello");
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  int mn = 1024;
  int mx = 0;

  for (int i = 0; i < 100; ++i) {
    int val = analogRead(microphonePin);
    //Serial.println(val);
    mn = min(mn, val);
    mx = max(mx, val);
  }

  int delta = mx - mn;

  //Serial.println(delta);

  if (delta > 200) {
    digitalWrite(LED_BUILTIN, HIGH);
    //Serial.println("Allume led");
    delay(1000);
  }

  else {
    digitalWrite(LED_BUILTIN, LOW);
  }
}

