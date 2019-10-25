distance_m = float(input("Enter your distance(m): "))
time_sec = float(input("Enter your time(sec): "))

def velocity(distance_m, time_sec):
    velocity = distance_m/time_sec
    return str(velocity) + " m/s"
print (velocity(distance_m, time_sec))