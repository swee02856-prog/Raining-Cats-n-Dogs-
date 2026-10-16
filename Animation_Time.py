frame = 0
timer = 0

clockframe = 0
clockframetimer = 0

def PlayerAnimation():
    global timer, frame
    if timer >= 450:
        frame = 1 - frame
        timer = 0

def ClockAnimation():
    global clockframetimer, clockframe
    if clockframetimer >= 2600:
        clockframe = 1 - clockframe
        clockframetimer = 0
