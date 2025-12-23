#The Smart Light Bulb
#Create a class LightBulb.
#__init__: Set self.is_on = False (lights start off).
#Method switch_on(): Set self.is_on = True.
#Method switch_off(): Set self.is_on = False.
#Method status(): Print "The light is ON" or "The light is OFF" based on the variable.

class LightBulb: 
    def __init__ (self):
        self.is_on = False
    
    def switch_on(self):
        self.is_on = True
        print(f"The state of bubl is {self.is_on}")

    def switch_off(self):
        self.is_on = False
        print(f"The state of bubl is {self.is_on}")

bulb = LightBulb()
bulb.switch_off()
bulb.switch_on()