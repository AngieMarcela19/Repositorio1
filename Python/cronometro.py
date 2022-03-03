import os
import time

for hora in range(24):
    for min in range(60):
        for segundos in range(60):
            os.system('cls')
            print(f'{hora}:{min}:{segundos}')
            time.sleep(1)