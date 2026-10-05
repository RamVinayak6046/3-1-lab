# Initial states
robot_location = "A"
ladder_location = "B"
tool_location = "C"
robot_has_tool = False
robot_on_ladder = False

print("Robot starting at", robot_location)

# Step 1: Move to ladder
robot_location = ladder_location
print("Robot picked up the ladder")
print("Robot moved to tool location", robot_location)
robot_on_ladder = True

# Step 2: Robot climbs and picks tool
print("Robot placed ladder and climbed up")
robot_has_tool = True
print("Robot picked tool from shelf")
robot_on_ladder = False

# Step 3: Climb down and goal check
print("Robot climbed down safely")
print("In Goal state Reached:")
print("Robot has tool:", robot_has_tool)
