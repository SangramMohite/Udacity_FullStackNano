import webbrowser
import time

counter = 0;
sleep_time = 5  # 2*60*60
while(counter < 3):
    print ("This program started at: " + time.ctime())
    time.sleep(sleep_time)
    webbrowser.open("https://www.youtube.com/watch?v=W3CDNpvWUkA")
    counter += 1
