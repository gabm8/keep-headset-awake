import winsound
import time
# Set frequency in Hertz
frequency = 18000
# Set duration in milliseconds
duration = 1000

while True:
    # Make beep sound on Windows
    winsound.Beep(frequency, duration)
    time.sleep(2*5)