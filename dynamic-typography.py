import graphics as g
from graphics import *

userInput = input('Enter your statement: ')
index = 1

win = g.GraphWin("Window", 400, 400)
win.setBackground('Gray')
for character in userInput:
    statement = Text(Point(10*index,ord(character)), character).draw(win)
    statement.setTextColor('Blue')
    index = index + 1
    

                       






