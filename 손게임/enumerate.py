balls = [(20,20), (60,60)]
import random
for idx, 좌표 in enumerate(balls):
    print(idx, 좌표)
new_x = random.randrange(20,1600,40)
new_y = random.randrange(20,1400,40)
balls.append((new_x,new_y))
print(balls)