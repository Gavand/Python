'''
    Author: Gavin Andrews
    Date: 02/08/18
    
    Description:
    This program imports the turtle graphics and shows the first three letters of my name in green.
    The program uses differnt functions to draw out each letter.
    '''

import turtle


#==========================================================
def draw_G(some_turtle):
    '''
        This function draws letter G.
        
        Parameter:
        some_turtle: turtle that is used to draw the letter G
        
        Returns: None
        '''
    some_turtle.forward(100)
    some_turtle.left(90)
    some_turtle.forward(100)
    some_turtle.left(90)
    some_turtle.forward(100)
    some_turtle.left(90)
    some_turtle.forward(50)
    some_turtle.left(90)
    some_turtle.forward(50)
    some_turtle.pendown()
    return None

def draw_A(some_turtle):
    '''
        This function draws letter A.
        
        Parameter:
        some_turtle: turtle that is used to draw the letter A
        
        Returns: None
        '''
    some_turtle.pendown()
    some_turtle.left(60)
    some_turtle.forward(60)
    some_turtle.right(180)
    some_turtle.forward(120)
    some_turtle.right(120)
    some_turtle.forward(120)
    some_turtle.penup()
    some_turtle.right(180)
    some_turtle.forward(30)
    some_turtle.left(60)
    some_turtle.pendown()
    some_turtle.forward(90)
    return None

def draw_V(some_turtle):
    '''
        This function draws letter V.
        
        Parameter:
        some_turtle: turtle that is used to draw the letter V
        
        Returns: None
        '''
    some_turtle.left(90)
    some_turtle.forward(20)
    some_turtle.right(150)
    some_turtle.pendown()
    some_turtle.forward(120)
    some_turtle.penup()
    some_turtle.right(180)
    some_turtle.forward(120)
    some_turtle.left(120)
    some_turtle.pendown()
    some_turtle.forward(120)
    some_turtle.right(60)
    return None


def skip(some_turtle, far):
    '''
        This function picks up the pen and sends the pen to the location of inputted integer.
        
        Parameter:
        some_turtle: turtle that is used to pick pen up and send to send to location
        far: function used to send the pen to the location of the inputted integer
        '''
    some_turtle.penup()
    some_turtle.fd(far)

#==========================================================
def main():
    '''
        Draws my nickname: "Gav"
        '''
    gturtle = turtle.Turtle()
    gturtle.pensize(10)
    gturtle.speed(0)
    gturtle.shape('turtle')
    gturtle.penup()
    gturtle.left(90)
    gturtle.forward(150)
    gturtle.left(90)
    gturtle.forward(200)
    gturtle.pendown()

    gturtle.pencolor("dark green")
    draw_G(gturtle)
    
    skip(gturtle, -100)

    gturtle.pencolor("dark green")
    draw_A(gturtle)
    
    skip(gturtle, -150)
    
    gturtle.pencolor("dark green")
    draw_V(gturtle)

    turtle.getscreen().exitonclick()

if __name__ == '__main__':
    main()
