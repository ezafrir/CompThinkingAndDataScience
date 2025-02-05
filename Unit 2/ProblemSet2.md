**Problem 1: RectangularRoom Class**

You will need to design two classes to keep track of which parts of the room have been cleaned as well as the position and direction of each robot.
In ps2.py, we've provided skeletons for the following two classes, which you will fill in in Problem 1:
RectangularRoom: Represents the space to be cleaned and keeps track of which tiles have been cleaned.
Position: We've also provided a complete implementation of this class. It stores the x- and y-coordinates of a robot in a room.
Read ps2.py carefully before starting, so that you understand the provided code and its capabilities.

Problem 1
In this problem you will implement the RectangularRoom class. For this class, decide what fields you will use and decide how the following operations are to be performed:

Initializing the object
Marking an appropriate tile as cleaned when a robot moves to a given position (casting floats to ints - and/or the function math.floor - may be useful to you here)
Determining if a given tile has been cleaned
Determining how many tiles there are in the room
Determining how many cleaned tiles there are in the room
Getting a random position in the room
Determining if a given position is in the room
Complete the RectangularRoom class by implementing its methods in ps2.py.

Although this problem has many parts, it should not take long once you have chosen how you wish to represent your data. For reasonable representations, a majority of the methods will require only a couple of lines of code.

**Problem 2: Robot Class**

In ps2.py we provided you with the Robot class, which stores the position and direction of a robot. For this class, decide what fields you will use and decide how the following operations are to be performed:

Initializing the object
Accessing the robot's position
Accessing the robot's direction
Setting the robot's position
Setting the robot's direction
Complete the Robot class by implementing its methods in ps2.py.

Note: When a Robot is initialized, it should clean the first tile it is initialized on. Generally the model these Robots will follow is that after a robot lands on a given tile, we will mark the entire tile as clean. This might not make sense if you're thinking about really large tiles, but as we make the size of the tiles smaller and smaller, this does actually become a pretty good approximation.

Note: The Robot class is an abstract class, which means that we will never make an instance of it. Read up on the Python docs on abstract classes at this link and if you want more examples on abstract classes, follow this link.

In the final implementation of Robot, not all methods will be implemented. Not to worry -- its subclass(es) will implement the method updatePositionAndClean()

**Problem 3: StandardRobot Class**

Each robot must also have some code that tells it how to move about a room, which will go in a method called updatePositionAndClean.
Ordinarily we would consider putting all the robot's methods in a single class. However, later in this problem set we'll consider robots with alternate movement strategies, to be implemented as different classes with the same interface. These classes will have a different implementation of updatePositionAndClean but are for the most part the same as the original robots. Therefore, we'd like to use inheritance to reduce the amount of duplicated code.
Complete the updatePositionAndClean method of StandardRobot to simulate the motion of the robot after a single time-step (as described on the Simulation Overview page).
