'''
    Author: Gavin Andrews
    Date: 02/08/18
    Class: ISTA 130
    Section Leader: Sebastian Andrews
    
    Description:
    This program creates an abstract shaped snake with turtle by using shape functions like
    triangle, square, hexagon, and pentagon.
    '''

import turtle


#==========================================================
def triangle(leo, a):
    '''
        This function draws five triangles.
        
        Parameters:
        leo: a turtle that is used to draw triangles
        a: an int that determines the length of each side of triangle
        
        Returns: None
        '''
    leo.left(90)
    leo.forward(100)
    leo.left(90)
    leo.forward(245)
    leo.right(90)
    leo.pendown()
    leo.forward(a)
    leo.left(120)
    leo.forward(a)
    leo.left(120)
    leo.forward(a)
    leo.left(30)
    leo.penup()
    leo.forward(a)
    leo.pencolor("dark green")
    leo.left(30)
    leo.pendown()
    leo.forward(a * 2)
    leo.right(120)
    leo.forward(a)
    leo.right(120)
    leo.forward(a * 2)
    leo.left(120)
    leo.forward(a)
    leo.penup()
    leo.left(120)
    leo.forward(a * 2)
    leo.right(60)
    leo.pendown()
    leo.forward(a * 2)
    leo.left(120)
    leo.forward(a)
    leo.left(120)
    leo.forward(a * 2)
    return None

def square(don, b):
    '''
        This function draws one square with a loop.
        
        Parameters:
        don: a turtle that is used to draw square
        b: an int that determines the length of each side of square
        
        Returns: None
        '''
    don.penup()
    don.right(30)
    don.forward(130)
    don.pendown()
    for i in range(4):
        don.forward(b)
        don.right(90)
    return None

def hexagon(ralph, c):
    '''
        This function draws two hexagons.
        
        Parameters:
        ralph: a turtle that is used to draw hexagons
        c: an int that determines the length of each side of hexagons
        
        Returns: None
        '''
    ralph.pendown()
    ralph.left(150)
    for i in range(6):
        ralph.forward(c)
        ralph.left(60)
    ralph.penup()
    for i in range(2):
        ralph.forward(c)
        ralph.left(60)
    ralph.pendown()
    for i in range(6):
        ralph.forward(c)
        ralph.right(60)
    return None

def pentagon(mikey, d):
    '''
        This function draws a pentagon.
        
        Parameters:
        mikey: a turtle that is used to draw pentagon
        d: an int that determines the length of each side of pentagon
        
        Returns: None
        '''
    mikey.penup()
    mikey.right(90)
    mikey.forward(130)
    mikey.right(18)
    mikey.pendown()
    for i in range(4):
        mikey.forward(d)
        mikey.left(72)
    mikey.forward(d)
    return None

#==========================================================
def main():
    '''
        Draws the full abstract snake by calling the shape functions.
        '''
    theturtle = turtle.Turtle()
    theturtle.pensize(10)
    theturtle.speed(0)
    theturtle.shape('turtle')
    theturtle.penup()

    theturtle.pencolor("black")
    triangle(theturtle, 75)

    theturtle.pencolor("red")
    square(theturtle, 75)

    theturtle.pencolor("black")
    hexagon(theturtle, 75)

    theturtle.pencolor("red")
    pentagon(theturtle, 75)

    turtle.getscreen().exitonclick()

if __name__ == '__main__':
    main()
