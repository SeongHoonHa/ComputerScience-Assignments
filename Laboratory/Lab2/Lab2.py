def speedometer(pos1, pos2, time):
    """
    Problem Description
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Calculate the speed of a moving car.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Input:
        pos1 - the initial position of the car
        pos2 - the final position of the car
        time - the recorded time the car spent between them
    Returns: The speed of the car.
    """
    # speed = distance/ time
    return abs(pos2 - pos1) / time


def warping(speed):
    """
    Problem Description
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    In the wonderful world of Star Trek, they have a way to travel faster than light. Below is a table of the speed representation. 
    The table is from "The Star Trek Encyclopedia: A Reference Guide to the Future. Updated and Expanded Edition" by Michael Okuda 
    and Denise Okuda.
    Speed                   |    Number of times speed of light (Number represents lower bound)
    Sublight(Warp Factor 0) |    0
    Warp Factor 1           |    1
    Warp Factor 2           |    10
    Warp Factor 3           |    39
    Warp Factor 4           |    102
    Warp Factor 5           |    214
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Input: A float or number
    Returns: A number representing the warp factor
    """
    if speed < 1:
        return 0
    elif speed < 10:
        return 1
    elif speed < 39:
        return 2
    elif speed < 102:
        return 3
    elif speed < 214:
        return 4
    else:
        return 5    



def catch_speeders(pos1, pos2, time):
    """
    Problem Description
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    You are a member of the Star Fleet space-travel law enforcement in the world of Star Trek.
    You have caught a ship -- the USS Enterprise -- speeding in the past, and you wish to catch
    them again.  The legal warp speed is 3 -- anything above this and you need to notify your
    superiors.  Write a function which signals whenever warp speed detected is above 3.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Input:
        pos1 - the initial position of the spaceship
        pos2 - the final position of the spaceship
        time - the recorded time
    Returns: A signal indicating that the warp factor exceeds 3.
    """
    # 1. get the speed
    speed = speedometer(pos1, pos2, time)
    # 2. Get the warp factor
    warpFactor = warping(speed)
    # 3. Check if they're speeding

    if warpFactor >3 :
        return "they're speeding"
    else:
        return "not speeding"

    #warping(speedometer(pos1, pos2, time))

def myTestString(func, params):
    """
    Do not modify
    """
    return func.__name__ + "" + str(params) + " produces " + str(func(*params))

# For more information about the line below, refer to the link: https://docs.python.org/3/library/__main__.html
#   You can read more about it but it is to help when handling multiple files
#   Will be dicussed at a later point
if __name__ == "__main__":
    print("Final Test Code\n")
    print("Testing speedometer()")
    for x in [(0.0,4.0,2.0), (-1,5,40), (0,0,1.0), (6,3,33)]:
        print(myTestString(speedometer, x))
    print("Testing warping()")
    for x in [(0,), (41.0,),(10.2,), (1111,)]:
        print(myTestString(warping, x))
    print("Testing catch_speeders()")
    for x in [(145,150,1.0), (125,150,1.0), (25,150,1.0), (5,150,1.0)]:
        print(myTestString(catch_speeders, x))