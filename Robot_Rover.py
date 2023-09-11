"""Robot_Rover controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Keyboard
# create the Robot instance.
robot = Robot()
keyboard = Keyboard()
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

wheel1_left = robot.getDevice("wheel1_left")
wheel1_left.setPosition(float('inf'))
wheel1_left.setVelocity(0.0)

wheel1_right = robot.getDevice("wheel1_right")
wheel1_right.setPosition(float('inf'))
wheel1_right.setVelocity(0.0)

wheel2_left = robot.getDevice("wheel2_left")
wheel2_left.setPosition(float('inf'))
wheel2_left.setVelocity(0.0)

wheel2_right = robot.getDevice("wheel2_right")
wheel2_right.setPosition(float('inf'))
wheel2_right.setVelocity(0.0)
timestep = 64
# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
speed = 4
keyboard.enable(timestep)
while robot.step(timestep) != -1:
    key_pressed = keyboard.getKey()
    print(key_pressed)
    if(key_pressed == 83)
        wheel1_left.setVelocity(speed)
        wheel1_right.setVelocity(speed)
        wheel2_left.setVelocity(speed)
        wheel2_right.setVelocity(speed)
    
    if(key_pressed == 87)
        wheel1_left.setVelocity(-speed)
        wheel1_right.setVelocity(-speed)
        wheel2_left.setVelocity(-speed)
        wheel2_right.setVelocity(-speed)
        
    if(key_pressed == 65)
        wheel1_left.setVelocity(-speed)
        wheel1_right.setVelocity(speed)
        wheel2_left.setVelocity(-speed)
        wheel2_right.setVelocity(speed)
        
    if(key_pressed == 68)
        wheel1_left.setVelocity(speed)
        wheel1_right.setVelocity(-speed)
        wheel2_left.setVelocity(speed)
        wheel2_right.setVelocity(-speed)
        
    if(key_pressed == -1)
        wheel1_left.setVelocity(0)
        wheel1_right.setVelocity(0)
        wheel2_left.setVelocity(0)
        wheel2_right.setVelocity(0)
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    

# Enter here exit cleanup code.
