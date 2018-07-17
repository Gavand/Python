text = 'Rocket!'

print('text:', text)

print('text[2]:', text[2])

print('text[-1] * 5:', text[-1] * 5)

mystery = text[-2] + text[0] + text[-3] + text[4]

m2 = mystery.upper()

print('text[-2] + text[0] + text[-3] + text[4]:', mystery)

print('mystery.upper():', m2)

print('m2 + m2.lower():', m2 + m2.lower())

print('m2 > m2.lower():', m2 > m2.lower())

print('m2 < m2.lower():', m2 < m2.lower())

print("'REE' in m2:", 'REE' in m2)

print("'REE' in m2.lower():", 'REE' in m2.lower())

print('\n***** indexed by i % 2 *****')

for i in range(len(text)):  # what kind of traversal is this?
    if i % 2 == 1:
        print(text[i])

print("\n***** ch > 'e' *****")

for ch in text:  # what kind of traversal is this?
    if ch > 'e':
        print(ch)

print()

def odds(string):
    '''
    This function takes one string argument (string) and returns
    a new string consisting of all of the odd position
    characters in the argument.
    '''
    new_str = ''
    for i in range(len(string)):  
        if i % 2 == 1:
            new_str += string[i]
    return new_str

print('odds:', odds(text))

def first_and_last(string):
    '''
    This function takes one string argument (string) and returns
    a new string consisting of the first and last character 
    in the argument.  It returns None if the argument
    is the empty string.
    '''
    if string: # same as: if string != '':
        return string[0] + string[-1]
    # return None - not necessary - Python does it for us
        

print('first_and_last: ', first_and_last(text))
print('first_and_last: ', first_and_last('A'))

def thirds(string):
    '''
    This function takes one string argument (string) and returns
    a new string consisting of every third
    character in the argument.  It returns None if the 
    string doesn't have at least three characters.
    '''
    if len(string) >= 3:
        new_str = ''
        for i in range(len(string)):  
            if (i + 1) % 3 == 0:
                new_str += string[i]
        return new_str

print('thirds:', thirds(text))
print('thirds:', thirds('12345678'))
print('thirds:', thirds('123456789'))

def count(string, ch):
    '''
    This function takes one nonempty string argument
    (string) and one one-character string (ch) and 
    returns the number of times ch occurs in string.
    '''
    total = 0
    for char in string:
        if char == ch:
            total += 1
    return total
    
print('count:', count(text, 'R'))
print('count:', count(text, 'r'))
print('count:', count('coca-cola', 'c'))

def smallest(string):
    '''
    This function takes one nonempty string argument (string) and returns
    a new the smallest character in the argument, not counting
    space, tab or newline.  Assume the first character is neither
    of those.
    '''
    small = string[0]
    for ch in string:
        if ch != ' ' and ch != '\t' and ch != '\n' and ch < small:
            small = ch
    return ch

print('smallest:', smallest(text))
print('smallest:', smallest('qQ'))
print('smallest:', smallest('q Q'))

def alphabetize(s1, s2, s3):
    '''
    This function takes three string arguments, s1, s2, and s3 and prints them 
    in alphabetical order, one per line, starting with the smallest.
    It returns None.
    '''
    if s1.lower() <= s2.lower():
        if s2.lower() <= s3.lower():
            print(s1 + '\n' + s2 + '\n' + s3)
        elif s1.lower() <= s3.lower():
            print(s1 + '\n' + s3 + '\n' + s2)
        else:
            print(s3 + '\n' + s1 + '\n' + s2)
    else:   # s2 < s1
        if s1.lower() <= s3.lower(): 
            print(s2 + '\n' + s1 + '\n' + s3)
        elif s3.lower() < s2.lower():
            print(s3 + '\n' + s2 + '\n' + s1)
        else:
            print(s2 + '\n' + s3 + '\n' + s1)
            
print('Should be: "heart", "I", then "Rocket"')
alphabetize("I", "heart", "Rocket")
    
def alphabetize2(s1, s2, s3):
    '''
    This function takes three string arguments, s1, s2, and s3 and prints them 
    in alphabetical order, one per line, starting with the smallest.
    It returns None.
    '''
    if s1.lower() <= s2.lower() <= s3.lower():
        print(s1 + '\n' + s2 + '\n' + s3)
    elif s1.lower() <= s3.lower() <= s2.lower():
        print(s1 + '\n' + s3 + '\n' + s2)
    elif s3.lower() <= s1.lower() <= s2.lower():
        print(s3 + '\n' + s1 + '\n' + s2)
    elif s2.lower() <= s1.lower() <= s3.lower(): 
        print(s2 + '\n' + s1 + '\n' + s3)
    elif s3.lower() < s2.lower() <= s1.lower():
        print(s3 + '\n' + s2 + '\n' + s1)
    else:
        print(s2 + '\n' + s3 + '\n' + s1)
            
print('Should be: "heart", "I", then "Rocket"')
alphabetize2("I", "heart", "Rocket")
    
print('Should be: "dog", "is", then "Rocket"')
alphabetize2("Rocket", "is", "dog")
    
    
    
    
    
