# WOW
This GitHub repo contains the programs and other required files that I have used to complete my WOW project. This markdown file will provide a brief description of the code files. I used Python 3.9.7 and Visual Studio Code.

## Old (Folder)
Contains the code for the original robot motion algorithm that used a single shot to detect and move to objects. No longer in use. It has to be run in the following order:
1. img.py
2. detection.py
3. rob.py
## robot.py
The up-to-date code file that makes use of classes, functions and variables from the urx library and wowclasses.py to implement the algorithm. This is geared towards 3 items but adding a loop will mitigate this problem.\
The file requires the following libraries:
`tensorflow >= 2.2, tensorflow-gpu >= 2.2 (match version with tensorflow), tensorflow_hub (latest), opencv-python (latest), numpy (latest), pandas (latest), urx (latest), time (latest)`
## wowclasses.py
Contains the code for movement, detection, and set-up. Used in robot.py.\
The file requires the following libraries:
`tensorflow >= 2.2, tensorflow-gpu >= 2.2 (match version with tensorflow), tensorflow_hub (latest), opencv-python (latest), numpy (latest), pandas (latest), urx (latest), time (latest)`
## test.py
Moves the robot to the home position (can be modified)
## pseudocode (file)
Contains the algorithm pseudocode.
