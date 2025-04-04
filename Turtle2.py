from turtle import Turtle, mainloop
import random


class AnimatedTurtle(Turtle):
    __allTurtles = []
    def __init__(self, hwall, vwall):
        super().__init__()
        self.__scr = self.getscreen()
        self.__xmin = -vwall + 10
        self.__xmax = vwall - 10
        self.__ymin = -hwall + 10
        self.__ymax = hwall - 10
        self.__scr.ontimer(self.__moveOneStep, 100)
        AnimatedTurtle.__allTurtles.append(self)

    def __moveOneStep(self):
        self.__computeNewHeading()
        self.forward(5)
        self.__checkCollisions()
        self.__scr.ontimer(self.__moveOneStep, 100)
        # ontimer is only called once when the interval expires

    def __computeNewHeading(self):
        xpos, ypos = self.position()
        oldHead = self.heading()
        newHead = oldHead

        if xpos > self.__xmax or xpos < self.__xmin:
            newHead = 180 - oldHead
        if ypos > self.__ymax or ypos < self.__ymin:
            newHead = 360 - oldHead
        if newHead != oldHead:
            self.setheading(newHead)

    def __checkCollisions(self):
        for otherT in AnimatedTurtle.__allTurtles:
            if self != otherT:
                if self.distance((otherT)) < 20:
                    tempHeading = self.heading()
                    self.setheading(otherT.heading())
                    otherT.setheading(tempHeading)
                    while self.distance(otherT) < 20:
                        self.forward(1)
                        otherT.forward(1)

#placing turtle with mouse clicks
from turtle import Turtle, mainloop
#from AnimatedTurtle import AnimatedTurtle
import random

class TurtlePlace:
    def __init__(self, t, hWall = 200, vWall = 200):
        self.__bigT = Turtle()
        self.__bigTScreen = self.__bigT.getscreen()
        self.__bigT.color('blue')
        self.__turtleList = []
        self.__bigTScreen.onclick(self.placeTurtle)
        self.__bigT.hideturtle()
        self.__numTurtles = 0
        self.__maxTurtle = t
        self.__hWall = hWall
        self.__vWall = vWall
        self.drawField()
        mainloop()

    def placeTurtle(self, x, y):
        newT = AnimatedTurtle(self.__hWall, self.__vWall) #new
        newT.hideturtle()
        newTscreen = newT.getscreen()
        newTscreen.tracer(0)
        newT.up()
        newT.goto(x, y)
        newT.shape('turtle')
        newT.color('green')
        newT.showturtle()
        newT.setheading(random.randint(1, 359))
        newTscreen.tracer(1)
        self.__numTurtles = self.__numTurtles + 1 #count
        self.__turtleList.append(newT)
        if self.__numTurtles >= self.__maxTurtle:
            self.__bigTScreen.onclick(None) #remove event handler

    def drawField(self):
        self.__bigTScreen.tracer(0)
        self.__bigT.up()
        self.__bigT.goto(-(self.__hWall), -(self.__vWall))
        self.__bigT.down
        for i in range(4):
            self.__bigT.forward(2 * self.__hWall)
            self.__bigT.left(90)
        self.__bigTScreen.tracer(1)

if __name__ == '__main__':
    t1 = TurtlePlace(10)


# # import sqlite3
# #
# #
# # def main():
# #     # Connect to the database.
# #     conn = sqlite3.connect('inventory.db')
# #
# #     # Get a cursor.
# #     cur = conn.cursor()
# #
# #     # Add the Inventory table.
# #     cur.execute('''CREATE TABLE Inventory (ItemID INTEGER NOT NULL PRIMARY KEY,
# #                                            ItemName TEXT,
# #                                            Price REAL)''')
# #
# #     # Commit the changes.
# #     conn.commit()
# #
# #     # Close the connection.
# #     conn.close()
# #
# #
# # # Execute the main function.
# # if __name__ == '__main__':
# #     main()
#
# import sqlite3
#
#
# def main():
#     # Connect to the database.
#     conn = sqlite3.connect('company.db')
#
#     # Get a cursor.
#     cur = conn.cursor()
#
#     # Add the Customer table.
#     cur.execute('''CREATE TABLE Customer (CustomerID INTEGER PRIMARY KEY,
#                                           Name TEXT,
#                                           Email TEXT)''')
#
#     # Add the Employee table.
#     cur.execute('''CREATE TABLE Employee (EmployeeID INTEGER PRIMARY KEY,
#                                           Name TEXT,
#                                           Position TEXT)''')
#
#     # Commit the changes.
#     conn.commit()
#
#     # Close the connection.
#     conn.close()
#
#
# # Execute the main function.
# if __name__ == '__main__':
#     main()

