
from func_ticker import *
from func_messages import *
from func_navigation import *

if __name__ == "__main__": 
    my_message = waypoint_messages("A")
    ticker(my_message)
    
    journey = "true"
    while journey == "true":
        ticker("Where?")
        userinput = input()
        
        ticker(waypoint_navigation("B", userinput))
        journey = "false"