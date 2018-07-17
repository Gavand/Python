'''
    Author: Gavin Andrews
    Date: 4/12/18
    Class: ISTA 130
    Section Leader: Sebastian Andrews
    
    Description:
    The function of this program is to read data from from a given file,
    collect the values into list, and then send information about animals
    to the user. The user is able to add/remove animals in a file, and
    when the data is finished being modified, the information is converted
    from kg and g to lbs and writes the data to a file.
    '''

def find_insert_position(str, ls):
    '''
    This function returns the position in a list of names in alphabetical order.
    
    str: The name of the mammal to search in list
    ls: The list of strings in alphabetical order
    '''
    
    element = [i.lower() for i in ls]
    element.append(str.lower())
    element = sorted(element)
    return element.index(str.lower())

def populate_lists(nameLs, bodyLs, brainLs):
    '''
    This function opens and read BrainBodyWeightKilos.csv and populates the list
    with the name, body weight, and brain weight.
    
    nameLs: The name in the list
    bodyLs: The body weight list
    brainLs: The brain weight list
    '''

    file = open("BrainBodyWeightKilos.csv", "r")
    lines = file.readlines()
    for line in lines[0:]:
        element = line.split(",")
        names = element[0].strip().title()
        nameLs.append(names)
        bodyLs.append(float(element[1]))
        brainLs.append(float(element[2]))

def write_converted_csv(file, nameLs, bodyLs, brainLs):
    '''
    This function opens a file and converts the weight into pounds then writes the
    data in a new file.
    
    file: The file to read
    nameLs: The name in the list
    bodyLs: The body weight in the list
    brainLs: The brain weight in the list
    '''

    file_read = open(file, 'w')
    for i in range(len(nameLs)):
        bodylbs = round(float(bodyLs[i]) * 2.205, 2)
        brainlbs = round(float(brainLs[i]) * 0.0022, 2)
        file_read.write(nameLs[i] + "," + str(bodylbs) + "," + str(brainlbs) + "\n")

#==========================================================
def main():
#    main()
    '''
    The main() function controls the adding, removing, and searching through the file
    and calls the functions accordingly.
    '''
    nameLs = []
    bodyLs = []
    brainLs = []

    populate_lists(nameLs, bodyLs, brainLs)
    while True:
        names = str(input('\nEnter animal name (or "q" to quit): '))
        names = names.title()
        if names.lower() == 'q':
            write_converted_csv("BrainBodyWeightPounds.csv", nameLs, bodyLs, brainLs)
            break
        if names in nameLs:
            i = nameLs.index(names)
            print(names+": "+"body = "+str(bodyLs[i])+", brain = "+str(brainLs[i]))
            delete = str(input('Delete "'+names+'"? (y|n)'))
            if delete == 'n':
                pass
            if delete == 'y':
                del nameLs[i];
                del brainLs[i];
                del bodyLs[i];
        elif names not in nameLs:
            print('File does not contain "'+names+'".')
            add = str(input('Add "'+names+'" to file? (y|n) '))
            if add == 'n':
                pass
            if add == 'y':
                bodyWt = str(input('Enter body weight for "'+names+'" in kilograms: '))
                brainWt = str(input('Enter brain weight for "'+names+'" in grams: '))
                element = find_insert_position(names, nameLs)
                nameLs.insert(element, names)
                brainLs.insert(element, brainWt)
                bodyLs.insert(element, bodyWt)

if __name__ == '__main__':
    main()
