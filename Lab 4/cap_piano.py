  
import time
import board
import busio

import adafruit_mpr121
import vlc

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

while True:
  
#    for i in range(12):
#       if mpr121[i].value:
#            print(f"Twizzler {i} touched!")

    if mp121[0].value:
             print(f"Twizzler 0 touched!")
             p = vlc.MediaPlayer("do.mp3")
             p.play()
    if mp121[1].value:
             print(f"Twizzler 1 touched!")
             p = vlc.MediaPlayer("do#.mp3")
             p.play()    
    if mp121[2].value:
             print(f"Twizzler 2 touched!")
             p = vlc.MediaPlayer("re.mp3")
             p.play()
    if mp121[3].value:
             print(f"Twizzler 3 touched!")
             p = vlc.MediaPlayer("re#.mp3")
             p.play()
    if mp121[4].value:
             print(f"Twizzler 4 touched!")
             p = vlc.MediaPlayer("mi.mp3")
             p.play()
    if mp121[5].value:
             print(f"Twizzler 5 touched!")
             p = vlc.MediaPlayer("fa.mp3")
             p.play()
    if mp121[6].value:
             print(f"Twizzler 6 touched!")
             p = vlc.MediaPlayer("fa#.mp3")
             p.play()
    if mp121[7].value:
             print(f"Twizzler 7 touched!")
             p = vlc.MediaPlayer("so.mp3")
             p.play()
    if mp121[8].value:
             print(f"Twizzler 8 touched!")
             p = vlc.MediaPlayer("so#.mp3")
             p.play()
    if mp121[9].value:
             print(f"Twizzler 9 touched!")
             p = vlc.MediaPlayer("la.mp3")
             p.play()
    if mp121[10].value:
             print(f"Twizzler 10 touched!")
             p = vlc.MediaPlayer("la#.mp3")
             p.play()
    if mp121[11].value:
             print(f"Twizzler 11 touched!")
             p = vlc.MediaPlayer("xi.mp3")
             p.play()
    time.sleep(0.25)  # Small delay to keep from spamming output messages.
