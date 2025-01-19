import random
import time
def obstacledistance():
    return random.uniform(1, 50)
def makealert(distance):
    if distance < 5:
        return "RED ALERT: Collision Imminent! Stop Immediately!"
    elif distance < 10:
        return "YELLOW ALERT: Danger Zone! Slow Down."
    elif distance < 20:
        return "GREEN ALERT: Safe Distance."
    else:
        return "No Alert: Clear Path."
def cranesdecision(distance):
    if distance < 5:
        return "Emergency Stop: The crane is stopping immediately."
    elif distance < 10:
        return "Slowing down: The crane is reducing speed."
    else:
        return "The crane is operating at normal speed."
def cranesoperation():
    while True:
        distance = obstacledistance()
        print(f"Obstacle detected at {distance:.2f} meters.")
        alert = makealert(distance)
        print(alert)
        decision = cranesdecision(distance)
        print(decision)
        time.sleep(2)
print("Starting crane operation simulation...\n")
cranesoperation()
