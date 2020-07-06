# know your power 

from adafruit_clue import clue
import analogio
import board
import time

pin = analogio.AnalogIn(board.A2)

def get_voltage(pin):
    return (pin.value * 3.3) / 65536
    
screen = clue.simple_text_display(text_scale=4, colors=(clue.ORANGE,))
screen[0].text = "know your"
screen[1].text = "power !"
screen[3].text = "in volt."
 
while True:
    screen[2].text = (round(get_voltage(pin),1))
    screen.show()
    time.sleep(0.1)
