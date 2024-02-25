from spotify_data import *
import time

print("starting powerhour")
skip_song()
for i in range(60):
    for j in range(60):
        time.sleep(1)
        print(str(60 - j) + " seconds left")

    skip_song()
    print("current shot count: "+str(i))
