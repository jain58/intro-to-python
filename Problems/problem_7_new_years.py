"""
Start at 10 seconds and count down until 1 and then print "Happy New Year! 🎉"
"""
import time
count = 10
while count>0:
    print (str(count))
    count = count -1
    time.sleep(0.3)
print('Happy New Year! 🎉')
