"""
Description: Practice Python using Turtle

Author: Brandon Scarano
Created: 4/14/26
Credit: Tutorial provided by Eric Pogue
Gemini CLI utilized for troubleshooting

"""
import turtle
import sys

print('Starting TurtleDraw...')

TEXTFILE = input("Enter the file you want read: ")

steven = turtle.Turtle()
screen = turtle.Screen()
root = screen.getcanvas().winfo_toplevel() # Forces turtle to top application om screen
root.attributes('-topmost', True) # Puts on top as soon as it runs
root.attributes('-topmost', False) # Prevents app from being locked in front of others
screen.setup(width = 450, height = 450)
steven.speed(0)
steven.penup()


try:
    turtleDrawTextfile = open(TEXTFILE, 'r') # 'r' = read mode
    print(f"\n---Contents of {TEXTFILE} ---")
        
except FileNotFoundError:
    print(f"Error: '{TEXTFILE}' was not found")
    sys.exit()

line = turtleDrawTextfile.readline()
while line:
    print(line, end='') # just prints the text file in terminal
    parts = line.split() 

    if(len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        steven.color(color) # make better
        steven.goto(x,y)
    # Todo: need to calculate total distance when we draw
        steven.pendown()

    if (len(parts) == 1): # assumes one input is stop
        steven.penup()

    line = turtleDrawTextfile.readline() # reads the next line in the loop

# Todo: print the total distance near the bottom right

# Allows user to press 'enter' to close turtle
screen.onkey(turtle.bye, "Return")
screen.listen()
turtle.done()

turtleDrawTextfile.close()
print('\nEnd')