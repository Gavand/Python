'''
    Author: Gavin Andrews
    Date: 2/22/18
    
    Description:
    This programs runs functions that tests simple conditional statements and return values.
    '''

def word_length(wd, num):
    '''
        This function prints the relationship between
        the inputted word and number.
        
        Parameters:
        wd: an string word that is inputted
        num: an int number length that is connected with the word
        '''
    if len(wd) > num:
        print("Longer than " + str(num) + " characters: " + wd)
    elif len(wd) == num:
        print("Exactly " + str(num) + " characters: " + wd)
    else:
        print("Shorter than " + str(num) + " characters: " + wd)

def stop_light(col, sec):
    '''
        This function returns the stop light that the light
        is supposed to turn to.
        
        col: a string color that is entered
        sec: an int amount of seconds to change to the next light
        '''
    if col == "green" and sec > 60:
        return "yellow"
    elif col == "yellow" and sec > 5:
        return "red"
    elif col == "red" and sec > 55:
        return "green"
    else:
        return col

def is_normal_blood_pressure(systolic, diastolic):
    '''
        This function returns true if the blood pressure is
        high or false if it is not between 120 and 80.
        
        systolic: an int amount that should be below 120
        diastolic: an int amount that should be below 80
        '''
    if systolic < 120 and diastolic < 80:
        return True
    else:
        return False

def doctor():
    '''
        This function prints if your blood pressure is normal
        or too high.
        '''
    systolic = int(input("Enter your systolic reading: "))
    diastolic = int(input("Enter your diastolic reading: "))
    
    if (is_normal_blood_pressure(systolic, diastolic) == True):
        print("Your blood pressure is normal.")
    else:
        print("Your blood pressure is high.")

def pants_size(waist):
    '''
        This function returns the size your waist is.
        
        waist: an int that determines your size
        '''
    if (waist >= 34):
        return "large"
    elif (waist >= 30):
        return "medium"
    else:
        return "small"

def pants_fitter():
    '''
        This function asks for your name, greets you, asks for your inches,
        how many pairs you like, and the type of pants.
        '''
    name = input("Enter your name: ")
    print("Greetings " + name + " welcome to Pants-R-Us")
    waist = int(input("Enter your waist size in inches: "))
    pair = int(input("How many pairs of pants would you like?"))
    pants = input("Would you like regular or fancy pants?")
    
    if (pants == "regular"):
        total = 40 * pair
        print(str(pair) + " pairs of " + str(pants_size(waist)) + " regular pants: $ " + str(total))
    elif (pants == "fancy"):
        total = 100 * pair
        print(str(pair) + " pairs of " + str(pants_size(waist)) + " fancy pants: $ " + str(total))

def digdug(num):
    '''
        This function evenly divides the inputted number and
        prints out digdug, dig, or dug.
        
        num: an int that is divided
        '''
    number = range(1, num + 1)
    for i in number:
        if i % 3 == 0 and i % 5 == 0:
            print(str(i) + " : " + "digdug")
        elif i % 3 == 0 and i % 5 != 0:
            print(str(i) + " : " + "dig")
        elif i % 3 != 0 and i % 5 == 0:
            print(str(i) + " : " + "dug")
        else:
            pass

def beef_type(percent_lean):
    '''
        This function compares the number to the
        percent of lean.
        
        percent_lean: an int the is compared to the percent of lean
        '''
    if percent_lean < 78:
        return "Hamburger"
    elif percent_lean >= 78 and percent_lean < 85:
        return "Chuck"
    elif percent_lean >= 85 and percent_lean < 90:
        return "Round"
    elif percent_lean <= 95 and percent_lean >= 90:
        return "Sirloin"
    else:
        return "Unknown"

def species_height(spec, num):
    '''
        This function compares the human and klingon height
        to their average heights and prints the relationship.
        
        spec: a string that inputs the type of species
        num: an int that inputs the height of the species
        '''
    avgHu = 67
    avgKl = 71

    if spec == "Human" and num > avgHu:
        print("Above Average")
    elif spec == "Human" and num < avgHu:
        print("Below Average")
    elif spec == "Human" and num == avgHu:
        print("Average")
    elif spec == "Klingon" and num > avgKl:
        print("Above Average")
    elif spec == "Klingon" and num < avgKl:
        print("Below Average")
    elif spec == "Klingon" and num == avgKl:
        print("Average")

def sooner_date(m1, d1, m2, d2):
    '''
        This function compares the first date to the second date
        and prints the sooner date.
        
        m1: an int that inputs the first month
        d1: an int that inputs the first day
        m2: an int that inputs the second month
        d2: an int that inputs the second day
        '''
    if m1 < m2 or m1 == m2 and d1 <= d2:
        print ("%d / %d" % (m1, d1))
    elif m1 > m2 or m1 == m2 and d1 >= d2:
        print ("%d / %d" % (m2, d2))

#==========================================================
if __name__ == '__main__':
    main()


