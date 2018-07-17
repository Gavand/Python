'''
    Author: Gavin Andrews
    Date: 02/16/18
    
    Description:
    This program runs eight functions that uses conversions and mathematical
    calculations by utilizing for loops, type casting, and operators.
    '''
import math

def print_word(num, wd):
    '''
        This function accepts a number and a word and prints out the
        the word the amount of times as the inputted number wiht a count.
        
        Parameters:
        num: an int to determines the amount of words to print
        wd: a string that determines the word to print
        '''
    num = int(num)
    wd = str(wd)
    for i in range(num):
        print(str(i + 1) + " --> " + wd)

def bacteria(min, gen):
    '''
        This function prints out the amount of bacteria that is
        left in a Petri dish as time goes by.
        
        Parameters:
        min: an int the passes the number in minutes
        gen: an int that prints the number of bacterial generations
        '''
    count = 2
    for i in range(gen):
        val = (i + 1) * min
        print("after " + str(val) + " minutes:  " + str(count) + " bacteria")
        count *= 2

def convert_to_copper(gp, sp, cp):
    '''
        This function combines copper, silver, and gold from the input,
        converts the coins into copper pieces, and prints the results.
        
        Parameters:
        gp: an int that determines the gold pieces
        sp: an int that determines the silver pieces
        cp: an int that determines the copper pieces
        '''
    silver = sp * 5
    gold = gp * 10 * 5
    
    total_cp = cp + silver + gold
    
    print(str(gp) + " gp, " + str(sp) + " sp, " + str(cp) + " cp converted to copper is: " + str(total_cp) + " cp")

def convert_from_copper(copper):
    '''
        This function takes the number of copper pieces and converts
        them the integer into gold, silver, and copper pieces.
        
        Parameters:
        copper: an int that determines the amount of inputted copper pieces
        '''
    gold = int(copper / 50)
    silver = int((copper - (gold * 50)) / 5)
    res = int(copper - (gold * 50) - (silver * 5))
    
    print (str(copper) + " copper pieces is: " + str(gold) + " gp, " +
           str(silver) + " sp, " +  str(res) + " cp")

def repeat_word(wd, rows, cols):
    '''
        This function prints out an inputted word in the amount
        of rows and cols inputted.
        
        Parameters:
        wd: a string that determines the word you want to repeat
        rows: an int that determines the amount of rows to repeat
        cols: an int that determines the amount of columns to repeat
        '''
    for i in range(rows):
        print(wd * cols)

def text_triangle(num):
    '''
        This function prints a triangle with letter X's in the amount
        that is entered in the num variable.
        
        Parameters:
        num: an int that determines how many X's you want to print
        '''
    for i in range(num):
        space = ''
        for j in range(i + 1):
            space+= str("x")
        print(space)
    if num <= 0:
        print("")

def surface_area_of_cylinder(rad, height):
    '''
        This function calculates the surface area of a cylinder and
        prints the surface area by being given the radius and height.
        
        Parameters:
        rad: an float that determines the radius of the cylinder
        height: an float that determines the height of the cylinder
        '''
    area = math.pi * pow(rad, 2)
    circum = 2 * math.pi * rad
    
    surface = (2 * area) + (circum * height)
    
    print("The surface area of a cylinder with radius " + str(float(rad)) +
          " and height " + str(float(height)) + " is " + str(surface))

def tree_height(dist, len):
    '''
        This function calculates the Pythagorean Theorem by using
        the given distance diagonally from the top of tree (hypotenuse) and
        the length away from the bottom of the tree (adjacent).
        
        Parameters:
        dist: a float that determines the distance from you to the base of tree
        len: a float that determines the length of the kite string
        '''
    tree = math.sqrt(pow(len, 2) - pow(dist, 2))
    
    print("Kite string: " + str(len) + "\n" + "Distance: " +
          str(dist) + "\n" + "Height: " + str(tree))
