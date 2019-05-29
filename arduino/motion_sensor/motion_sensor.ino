int ledPin = 4;                // choose the pin for the LED
int inputPin = 2;               // choose the input pin (for PIR sensor)
int pirState = LOW;             // we start, assuming no motion detected
int val = 0;                  // variable for reading the pin status
int num = 1;
 
void setup() {
  pinMode(ledPin, OUTPUT);      // declare LED as output
  pinMode(inputPin, INPUT);     // declare sensor as input
 
  Serial.begin(9600);
}
 
void loop(){
  
  val = digitalRead(inputPin);  // read input value

  //Serial.println("test1");
  if (val == HIGH) {            // check if the input is HIGH
    digitalWrite(ledPin, HIGH);  // turn LED ON
                      // wait for 5 sec
   
   

    
    if (pirState == LOW) {
      // we have just turned on
      //Serial.println("Motion detected!");
      // We only want to print on the output change, not state
      pirState = HIGH;
      Serial.println(pirState);
      
        val=LOW;
    }
   
  } else {
                  
    digitalWrite(ledPin, LOW); // turn LED OFF
     
    if (pirState == HIGH){
      // we have just turned of  
       
      // We only want to print on the output change, not state
      pirState = LOW;
      Serial.println(pirState);
      
    }
  }
   
}
