const int buzzerPin = 8;
const int ledPin = 9;

void setup() {
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  // Ouvre le port série pour écouter Python
  Serial.begin(9600); 
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    if (command == '1') {
      digitalWrite(ledPin, HIGH); // Allume la LED
      tone(buzzerPin, 1000);      // Fait sonner le buzzer à 1000Hz
    } 
    else if (command == '0') {
      digitalWrite(ledPin, LOW);  // Eteint la LED
      noTone(buzzerPin);          // Coupe le son
    }
  }
}
