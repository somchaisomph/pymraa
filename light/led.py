import mraa
import time
import threading

class LED(threading.Thread):
     def __init__(self,pin_number):
          threading.Thread.__init__(self)
          try:
               self._led = mraa.Gpio(pin_number)
               self._led.dir(mraa.DIR_OUT)
               self.stop_flag = False
          except :
               raise
               
    
