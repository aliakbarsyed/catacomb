def waypoint_navigation(waypointx, directionx):
    if waypointx == "B":
        turnings = {
            "forward": "",
            "left": "C",
            "right": "D"
        }
    elif waypointx == "C":
        turnings = {
            "forward": "E",
            "left": "",
            "right": ""
        }
        
    return turnings[directionx]
