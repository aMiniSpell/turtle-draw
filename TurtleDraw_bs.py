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
root = screen.getcanvas().winfo_toplevel()
root.attributes('-topmost', True)
root.attributes('-topmost', False)
screen.setup(width = 450, height = 450)
steven.speed(0)
steven.penup()


try:
    turtleDrawTextfile = open(TEXTFILE, 'r') # 'r' = read mode
    #with open(TEXTFILE, 'r') as file:
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

    line = turtleDrawTextfile.readline()

# Todo: print the total distance near the bottom right
turtle.done()
turtleDrawTextfile.close()

# Todo: wait for the user to press the enter key to terminate

print('\nEnd')