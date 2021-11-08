#Benjamin Shelton       November 5, 2021
# This program calculates the distance a suspended object falls
print("This program calculates the distance a suspended object falls.")
print("")
# Get gravity from user
gravity=input("What is the gravity? ")
# Convert string to int
gravity=int(gravity)
# Get fps from user
fps=input("What is the pixels per second ^2 (squared?) ")
# Convert string to int
fps=int(fps)
# Get number of frames from user
frames=input("What is the total amount of frames? ")
# Convert string to int
frames=int(frames)
# Calculate time object is falling
time=(frames/fps)
# Calculate distance in pixels object has fallen
distance=(.5*gravity*time**2)
print("It will drop", distance, "pixels in", time,"seconds")
