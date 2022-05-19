import os
import queue
import sounddevice as sd
import vosk
import sys
import pyautogui
import os

q = queue.Queue()

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


try:
    model = vosk.Model("en_US")
    with sd.RawInputStream(samplerate=44100, blocksize = 16000, device=None, dtype='int16',
                            channels=1, callback=callback):

            rec = vosk.KaldiRecognizer(model, 44100)
            os.system('echo 1 | sudo tee /sys/class/leds/input0\:\:capslock/brightness')
            #enables caps lock led for more fancy idk 
            while True:
                data = q.get()
                if not rec.AcceptWaveform(data):
                    #print(rec.PartialResult()[17:-3])
                    pass
                else:
                    os.system('echo 0 | sudo tee /sys/class/leds/input0\:\:capslock/brightness')
                    #disables led
                    phrase = (rec.Result())
                    ph = (' ' + phrase[14:-3] + ' ')
                    pyautogui.write(ph, interval=0.01)
                    sys.exit()
                    


except KeyboardInterrupt:
    sys.exit(0)
except Exception as e:
    sys.exit(type(e).__name__ + ': ' + str(e))
    #idk it only accepts int but should i care?
