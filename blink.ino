const int ledPin =  7;// the number of the LED pin
int ledState = LOW;             // ledState used to set the LED
unsigned long previous = 0;        // will store last time LED was updated
const long interval = 1000;           // interval at which to blink (microseconds)

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  unsigned long current = micros();

  if (current - previous >= interval) {
    previous = current;

    if (ledState == LOW) {
      ledState = HIGH;
    } else {
      ledState = LOW;
    }

    digitalWrite(ledPin, ledState);
  }
}
