from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


from usys import stdin
from uselect import poll

hub = PrimeHub()
hub.display.orientation(Side.LEFT)


hub.speaker.volume(20)
#hub.speaker.play_notes(Tetris, 120)

keyboard = poll()
keyboard.register(stdin)

while True:
    if keyboard.poll(0):
        key = stdin.read(1)
        print(key)
        if key == 'a':
            hub.speaker.beep()
        elif key == 'w':
            hub.speaker.beep(1000)
        elif key == 's':
            hub.speaker.beep(2000)

wait(1000)