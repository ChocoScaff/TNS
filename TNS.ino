const int microphonePin = A0;
int ledPin = 10;

void setup() {
  Serial.begin(9600);
  Serial.write("Hello")
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int mn = 1024;
  int mx = 0;

  for (int i = 0; i < 100; ++i) {
    int val = analogRead(microphonePin);
    mn = min(mn, val);
    mx = max(mx, val);
  }

  int delta = mx - mn;

  Serial.println(delta);

  if (delta > 200) {
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.write("Allume led");
    delay(1000);
  }

  else {
    digitalWrite(LED_BUILTIN, LOW);
  }
}