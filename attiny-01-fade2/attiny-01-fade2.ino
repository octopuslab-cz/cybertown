/*
attiny-01-blink.ino
Octopus engine - oeLAB - 2018/07 TEST (916B)

                Attiny 13/85 
                RST =--U--= VCC         oeLAB dev board1                  
 > pinAn/Rx (A) P3 =     = P2 (A1) (3) i2c Clock 
        /Tx (A) P4 =     = P1 /    (2) > LED 
               GND =     = P0 /  > (1) i2c Data 
*/
#define LED1_PIN        1  //LED_BUILTIN = Led2            
#define LED2_PIN        2  //
#define SPEED_FADE     10
#define PWM_MAX       255  // /5

// the setup function runs once when you press reset or power the board
void setup() {  
  pinMode(LED1_PIN, OUTPUT); // initialize digital pin as an output
  pinMode(LED2_PIN, OUTPUT);
  digitalWrite(LED2_PIN, HIGH);
  digitalWrite(LED1_PIN, LOW);
}


void fade2in(int led1,int led2) {  
  for (uint8_t i = 0; i < PWM_MAX; i++)
  { 
    analogWrite(led1, i);
    analogWrite(led2, (PWM_MAX-i));
    delay(SPEED_FADE);
  }
  digitalWrite(led1, HIGH);
  digitalWrite(led2, LOW); 
}
  

void fade2out(int led1,int led2) {
  for (uint8_t i = 0; i < PWM_MAX; i++)
  { 
    analogWrite(led1, (PWM_MAX-i));
    analogWrite(led2, i);
    delay(SPEED_FADE);
  }
  digitalWrite(led2, HIGH);
  digitalWrite(led1, LOW); 
}

unsigned long m_w = 1;
unsigned long m_z = 2; 

unsigned long getRandom()
{
    m_z = 36969L * (m_z & 65535L) + (m_z >> 16);
    m_w = 18000L * (m_w & 65535L) + (m_w >> 16);
    return (m_z << 16) + m_w;  /* 32-bit result /10*/
}


// the loop function runs over and over again forever
void loop() {
  fade2in(LED1_PIN,LED2_PIN); // delay(getRandom()*lightTime);
  //delay(getRandom());
  delay(2500);
  
  fade2out(LED1_PIN,LED2_PIN);
  //delay(getRandom()); 
  delay(2500);               
}
