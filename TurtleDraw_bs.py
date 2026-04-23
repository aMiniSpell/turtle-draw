"""
Description: Practice Python using Turtle

Author: Brandon Scarano
Created: 4/14/26
Credit: Tutorial provided by Eric Pogue
Gemini CLI utilized for troubleshooting

"""
import turtle
import sys
import math
import os


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
d_total = 0
while line:
    print(line, end='') # just prints the text file in terminal
    parts = line.split() 

    if(len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])
        if steven.isdown():
            d_total += steven.distance(x,y) # shorthand for adding current distance with the next one

        steven.color(color)
        steven.goto(x,y)
        steven.pendown()

    else:
        (len(parts) == 1) # assumes one input is stop
        steven.penup()

    line = turtleDrawTextfile.readline() # reads the next line in the loop

# Moves to write the total distance without drawing to that point
steven.penup()
steven.goto(55,-180)
steven.write(f"Total Distance Drawn: {d_total:.2f}")
# removes cursor to see image clearly
steven.hideturtle()

# Allows user to press 'enter' to close turtle
screen.onkey(turtle.bye, "Return")
screen.listen()
turtle.done()

turtleDrawTextfile.close()
print('\nEnd')