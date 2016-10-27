import mraa
import asyncio
#Tested with only python 3.4 installed on Raspbian
@asyncio.coroutine
def operate():
  global sw, led
  state = sw.read() # sw waits for signal flowing from pin 1 every time switch is pressed
  led.write(state)
  yield from asyncio.sleep(0.1)
  asyncio.async(operate())
  
if __name__ == "__main__":
  sw = mraa.Gpio(12) # attach pin 12 to one pin of switch
  led = mraa.Gpio(40) # attach pin 40 to LED
  sw.dir(mraa.DIR_IN) 
  led.dir(mraa.DIR_OUT) 
  loop = asynio.get_event_loop()
  try:
    asyncio.async(operate()) #prepare calling operate function
    loop.run_for_ever() # enter eternal loop 
  except KeyboardInterrupt : # loop is broken when user press Ctrl-C
    pass
  finally:
    loop.close() # finally loop is completely closed.

