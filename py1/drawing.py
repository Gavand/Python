'''
    Author: Gavin Andrews
    Date: 02/08/18
    
    Description:
    This program draws an abstract picture with abstract shapes using abstract shape functions.
    '''
import turtle

def circle(pencil):
    '''
        This function draws multiple black circles using a for loop.
        
        Parameters:
        pencil: a turtle that is used to draw circles
        
        Returns: None
        '''
    for i in range(5, 400, 50):
        pencil.right(90)
        pencil.forward(i)
        pencil.right(270)
        pencil.pendown()
        pencil.circle(i)
        pencil.penup()
    return None

def abstract(pen, b):
    '''
        This function draws multiple contours that forms a red abstract pattern.
        
        Parameters:
        pen: a turtle that is used to draw pattern
        b: an int that determines the length of each side of pattern
        
        Returns: None
        '''
    pen.home()
    pen.pendown()
    for i in range(16):
        pen.forward(b)
        pen.left(100)
        pen.forward(b)
    pen.penup()
    return None

def rect(mark, c):
    '''
        This function draws a green rectangle.
        
        Parameters:
        mark: a turtle that is used to draw rectangle
        c: an int that determines the length of each side of rectangle
        
        Returns: None
        '''
    mark.home()
    mark.forward(200)
    mark.left(90)
    mark.pendown()
    mark.forward(200)
    mark.left(90)
    mark.forward(400)
    mark.left(90)
    mark.forward(200)
    mark.left(90)
    mark.forward(400)
    return None

def draw(brush, d):
    '''
        This function draws another abstract shape using a for loop.
        
        Parameters:
        brush: a turtle that is used to draw abstract pattern
        d: an int that determines the length of each side of patterns
        
        Returns: None
        '''
    brush.home()
    brush.pendown()
    for i in range(40):
        brush.forward(200)
        brush.left(170)
        brush.forward(200)
    return None
#==========================================================
def main():
    '''
        Draws the abstract picture with different colors.
        '''
    theturtle = turtle.Turtle()
    theturtle.pensize(10)
    theturtle.speed(0)
    theturtle.shape('turtle')
    theturtle.penup()
    
    theturtle.pencolor("black")
    circle(theturtle)
    
    theturtle.pencolor("red")
    abstract(theturtle, 150)
    
    theturtle.pencolor("green")
    rect(theturtle, 150)
    
    theturtle.pencolor("blue")
    draw(theturtle, 150)

    turtle.getscreen().exitonclick()

if __name__ == '__main__':
    main()
