def print_time(hours):
    print("Day: " + str(round(hours / 24)))
    time = hours % 24
    if time > 12:
        print("Time: " + str(time - 12) + "pm")
    else:
        print("Time: " + str(time) + "am")
    if is_day(hours):
        print("It's daytime.")
    else:
        print("It's nighttime.")

def is_day(hours):
    time = hours % 24
    if time > 7 and time < 21:
        return True
    return False