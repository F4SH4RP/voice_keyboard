# voice_keyboard

# installation

pip3 install --user sounddevice vosk pyautogui 

then download some models from https://alphacephei.com/vosk/models

and in code on string 19 where its

model = vosk.Model("ru_RU")

specify a path to this model's folder (yes, unpack zip to foler first)

# use

en.py is for english or any other language which uses english alphabet. it prints text with pyautogui

ru.py is for other languages, since pyautogui dont type russian letters by default and i dont want to rtfm, it uses xdotool instead

so maybe do apt install xdotool

and just bind `python3 ~/Downloads/en.py` to some button

it will listen to mic and recognise speech untill u shut up for 1 second, then it types text.

# important

if ur sudo requires a password then either make caps led in /sys/ writeable with chmod 777 or just remove these strings where it says enable\disable caps lock led. 

i just like when it indicates when it listens to me, and its also fancy xd
