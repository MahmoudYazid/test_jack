from signal import pause
from gpiozero import Servo
from time import sleep
from gpiozero import LED

# servos movements
#gpio21 -> breathing
#gpio20 -> wt
#gpio 16 -> glucose
# gpio26 -> size (leg) = edema
# gpio19 ->eye contract
# gpio13 ->pigmentation(rash)= sequance of leds
#gpio 6 ->buzzer , vib. motor (bp)
#gpio 5 -> move pin (convulsion) 
#_______________________________

# servos control fluids
#gpio12 -> urination
#gpio25 -> feces
#gpio24 -> vomit
#gpio23 -> nasal mucus
#gpio22 -> ear fluid
#_________
#others
#thermia=27


breathing_pins=21  
wt_pins=20
glucose_pins=16
size_pins=26
eye_pins=19 
pigmentation_pins=13
bp_pins=6 
move_pins=5 
urination_pins=12
feces_pins=25
vomit_pins=24 
nasal_pins=23
ear_pins=22
thermia_pins=27






def high_on_pin(pin):
    pin_=LED(pin)
    pin_.on()
def low_on_pin(pin):
    pin_=LED(pin)
    pin_.off()

def control_servo_vib(state,pin):

    servo = Servo(pin)

    if state=="hyper":

        while number_of_sec>5:
            servo.min()
            sleep(0.5)
        
            servo.max()
            sleep(0.5)


        if state=="hypo":

        
            servo.min()
            sleep(5)
        
            servo.max()
            sleep(5)


        if state=="normal":

        
            servo.min()
            sleep(2.5)
        
            servo.max()
            sleep(2.5)


def control_servo_not_vib(state,pin):

    servo = Servo(pin)

    if state=="hyper":


        servo.max()
        sleep(0.5)


    if state=="hypo":


        servo.min()
        sleep(5)

    if state=="normal":


        servo.mid()
        sleep(2.5)



class normal :
    state_of_class="normal"
    def make_all(self,place_of_fluid):
        normal().breathing()
        normal().eye()
        normal().fluid(place=place_of_fluid)
        normal().move()
        normal().feces()
        normal().size()
        normal().urine()
        normal().pigmentation()
        normal().BP()
        normal().glucose()
        normal().thermia()
        normal().wt()        
    def breathing(self):
        control_servo_vib(state="{}".format(state_of_class), pin=breathing_pins)
    def thermia(self):
        low_on_pin(pin=thermia_pins)
    def wt(self):
        control_servo_not_vib(state="{}".format(state_of_class), pin=wt_pins)
    def move(self):
        control_servo_vib(state="{}".format(state_of_class), pin=move_pins)
        
    def eye(self):
        control_servo_not_vib(state="{}".format(state_of_class), pin=eye_pins)
        
    def pigmentation(self):
        low_on_pin(pin=pigmentation_pins)
        
    def fluid(self,place):
        if place=="nose":
            control_servo_not_vib(state="{}".format(state_of_class), pin=nasal_pins)
            
            
        if place=="mouth":
            control_servo_not_vib(state="{}".format(state_of_class), pin=vomit_pins)
            
        if place=="ear":
            control_servo_not_vib(state="{}".format(state_of_class), pin=ear_pins)
            

        
    def feces(self):
        control_servo_not_vib(state="{}".format(state_of_class), pin=feces_pins)
        
    def urine(self):

        control_servo_not_vib(state="{}".format(state_of_class), pin=urination_pins)
    def size(self):
        control_servo_not_vib(state="{}".format(state_of_class), pin=size_pins)
        
    def glucose(self):

        control_servo_not_vib(state="{}".format(state_of_class), pin=glucose_pins)

    def BP(self):
        #buzzer
        from gpiozero import PWMLED
        led = PWMLED(bp_pins)
        led.pulse()
        pause()

       
class hypo:
    state_of_class = "hypo"

    def make_all(self,place_of_fluid):
        hypo().breathing()
        hypo().eye()
        hypo().fluid(place=place_of_fluid)
        hypo().move()
        hypo().feces()
        hypo().size()
        hypo().urine()
        hypo().pigmentation()
        hypo().BP()
        hypo().glucose()
        hypo().thermia()
        hypo().wt()

    def breathing(self):
        control_servo_vib(state="{}".format(
            state_of_class), pin=breathing_pins)

    def thermia(self):
        low_on_pin(pin=thermia_pins)

    def wt(self):
        control_servo_not_vib(state="{}".format(state_of_class), pin=wt_pins)

    def move(self):
        control_servo_vib(state="{}".format(state_of_class), pin=move_pins)

    def eye(self):
        control_servo_not_vib(state="{}".format(state_of_class), pin=eye_pins)

    def pigmentation(self):
        low_on_pin(pin=pigmentation_pins)

    def fluid(self, place):
        if place == "nose":
            control_servo_not_vib(state="{}".format(
                state_of_class), pin=nasal_pins)

        if place == "mouth":
            control_servo_not_vib(state="{}".format(
                state_of_class), pin=vomit_pins)

        if place == "ear":
            control_servo_not_vib(state="{}".format(
                state_of_class), pin=ear_pins)

    def feces(self):
        control_servo_not_vib(state="{}".format(
            state_of_class), pin=feces_pins)

    def urine(self):

        control_servo_not_vib(state="{}".format(
            state_of_class), pin=urination_pins)

    def size(self):
        control_servo_not_vib(state="{}".format(state_of_class), pin=size_pins)

    def glucose(self):

        control_servo_not_vib(state="{}".format(
            state_of_class), pin=glucose_pins)

    def BP(self):
        #buzzer
        from gpiozero import PWMLED
        led = PWMLED(bp_pins)
        led.pulse()
        pause()


class hyper:
    state_of_class = "hyper"

    def make_all(self,place_of_fluid):
        hyper().breathing()
        hyper().eye()
        hyper().fluid(place_of_fluid)
        hyper().move()
        hyper().feces()
        hyper().size()
        hyper().urine()
        hyper().pigmentation()
        hyper().BP()
        hyper().glucose()
        hyper().thermia()
        hyper().wt()

    def breathing(self):
        control_servo_vib(state="{}".format(
            state_of_class), pin=breathing_pins)

    def thermia(self):
        high_on_pin(pin=thermia_pins)

    def wt(self):
        control_servo_not_vib(state="{}".format(state_of_class), pin=wt_pins)

    def move(self):
        control_servo_vib(state="{}".format(state_of_class), pin=move_pins)

    def eye(self):
        control_servo_not_vib(state="{}".format(state_of_class), pin=eye_pins)

    def pigmentation(self):
        high_on_pin(pin=pigmentation_pins)

    def fluid(self, place):
        if place == "nose":
            control_servo_not_vib(state="{}".format(
                state_of_class), pin=nasal_pins)

        if place == "mouth":
            control_servo_not_vib(state="{}".format(
                state_of_class), pin=vomit_pins)

        if place == "ear":
            control_servo_not_vib(state="{}".format(
                state_of_class), pin=ear_pins)

    def feces(self):
        control_servo_not_vib(state="{}".format(
            state_of_class), pin=feces_pins)

    def urine(self):

        control_servo_not_vib(state="{}".format(
            state_of_class), pin=urination_pins)

    def size(self):
        control_servo_not_vib(state="{}".format(state_of_class), pin=size_pins)

    def glucose(self):

        control_servo_not_vib(state="{}".format(
            state_of_class), pin=glucose_pins)

    def BP(self):
        #buzzer
        from gpiozero import PWMLED
        led = PWMLED(bp_pins)
        led.pulse()
        pause()


def make_func_automatic(array):

    for ex in array:
        print(ex)
        if "respiration" == "{}".format(ex[0]):
            if ex[1] == "1":
                hyper().breathing()
                
            if ex[1] == "0":
                normal().breathing()
            if ex[1] == "-1":
                hypo().breathing()

            
            

        if "eye" == "{}".format(ex[0]):
            if ex[1] == "1":
                hyper().eye()
                
            if ex[1] == "0":
                normal().eye()
            if ex[1] == "-1":
                hypo().eye()

            
            

        if "fluid" == "{}".format(ex[0]):
            if ex[1] == "1":
                hyper().fluid(place=ex[2])
                return 0
            if ex[1] == "0":
                normal().fluid(place=ex[2])
                return 0
            if ex[1] == "-1":
                hypo().fluid(place=ex[2])
                return 0

            
            

        if "move" == "{}".format(ex[0]):
            if ex[1] == "1":
                hyper().move()
                return 0
            if ex[1] == "0":
                normal().move()
                return 0
            if ex[1] == "-1":
                hypo().move()
                return 0

            
            return 0
        if "feces" == "{}".format(ex[0]):
            if ex[1] == "1":
                hyper().feces()
                return 0
            if ex[1] == "0":
                normal().feces()
                return 0
            if ex[1] == "-1":
                hypo().feces()
                return 0

            
            return 0
        if "size" == "{}".format(ex[0]):
            if ex[1] == "1":
                hyper().size()
                return 0
            if ex[1] == "0":
                normal().size()
                return 0
            if ex[1] == "-1":
                hypo().size()
                return 0

            
            return 0
        if "urine" == "{}".format(ex[0]):
            if ex[1] == "1":
                hyper().urine()
                return 0
            if ex[1] == "0":
                normal().urine()
                return 0
            if ex[1] == "-1":
                hypo().urine()
                return 0

            
            

        if "pigmentation" == "{}".format(ex[0]):
            if ex[1] == "1":
                hyper().pigmentation()
                return 0
            if ex[1] == "0":
                normal().pigmentation()
                return 0
            if ex[1] == "-1":
                hypo().pigmentation()
                return 0

            
            

        if "BP" == "{}".format(ex[0]):
            if ex[1] == "1":
                hyper().BP()
                return 0
            if ex[1] == "0":
                normal().BP()
                return 0
            if ex[1] == "-1":
                hypo().BP()
                return 0


        if "glucose" == "{}".format(ex[0]):
            if ex[1] == "1":
                hyper().glucose()
                return 0
            if ex[1] == "0":
                normal().glucose()
                return 0
            if ex[1] == "-1":
                hypo().glucose()
                return 0

            

        if "thermia" == "{}".format(ex[0]):
            if ex[1] == "1":
                hyper().thermia()
                return 0
            if ex[1] == "0":
                normal().thermia()
                return 0
            if ex[1] == "-1":
                hypo().thermia()
                return 0



        if "wt" == "{}".format(ex[0]):
            if ex[1] == "1":
                hyper().wt()
                return 0
            if ex[1] == "0":
                normal().wt()
                return 0
            if ex[1] == "-1":
                hypo().wt()
                return 0

            
