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
               
     def run(self):
          self.stop_flag = False
          while not self.stop_flag :
               pass
          
     def blink(self,interval=0.1,times=2):
          for i in range(times):
               self._led.write(1)
               time.sleep(interval)
               self._led.write(0)
               time.sleep(interval)
               
     def end(self):
          self.stop_flag = True
          self.join()
          
          
          
if __name__ == "__main__":
     led = LED(37) # connect pin 37 to LED
     led.start()
     for i in range(5):
          led.blink(interval=0.5,times=5) 
     led.end()
