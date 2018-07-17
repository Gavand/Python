import turtle, random
from worksheet_math_squares_line import random_color, square
        
def roots(a, b, c):
    '''
    roots determines and prints the roots of a quadratic equation with 
    coefficients a, b, and c.  It returns None.
    '''
    discriminant = b**2 - 4 * a * c
    print("discriminant:", discriminant)
    root_disc = math.sqrt(discriminant)
    root1 = (-b + root_disc) / (2 * a)
    root2 = (-b - root_disc) / (2 * a)
    print(root1, root2)
    
def main():
    '''
    Draw a number determined by the user of 
    squares of random color in random places.
    '''
    azt = turtle.Turtle()
    turtle.bgcolor('black')
    azt.shape('turtle')
    azt.speed(0)
    azt.pensize(5)
    for i in range(100):
        random_color(azt)
        x = random.randrange(701) - 400
        y = random.randrange(501) - 300
        azt.penup()
        azt.goto(x, y)
        azt.pendown()
        azt.begin_fill()
        square(azt, random.randint(1, 100))
        azt.end_fill()
        
    turtle.getscreen().exitonclick()
        
if __name__ == "__main__":
    main()