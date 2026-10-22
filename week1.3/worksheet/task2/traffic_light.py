"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"
time_in_state = 0


# Simulate the traffic light system up to time=maxtime in 1-second steps
 
for time in range(maxtime + 1):

    cycle = time % 15

    if cycle <= 3:
        state = "red"
    elif cycle <= 6:
        state = "red_amber"
    elif cycle <= 11:
        state = "green"
    else:
        state = "amber"

    print(f"Time {time:03d} State {state}")