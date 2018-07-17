'''
    Author: Gavin Andrews
    Date: 4/19/18
    Class: ISTA 130
    Section Leader: Sebastian Andrews
    
    Description:
    The function of this program is to read a file, create a dictionary containing
    a description of fish with the observation, name, species, weight, length, height, width, and
    sex. Prints a report by reading the file, sending the number, name, and weight into a dictionary.
    '''

def fish_dict_from_file(file):
    '''
    This function reads the file ('fishcatch.dat'), makes a dictionary map
    of the species with a value, creates a an empty dictionary, and writes/returns
    a dictionary with the names and weights of the fish.
        
    file: the file to read the desciption of fish ('fishcatch.dat')
    '''
    
    file_reader = open(file, 'r')
    fishmap = {'1' : 'Bream', '2' : 'Whitefish', '3' : 'Roach','4' : '?','5' : 'Smelt','6' : 'Pike','7' : 'Perch'}
    dict = {}
    for line in file_reader:
        fish = line.split()
        count = fish[0]
        species = fish[1]
        weight = fish[2]
        if fishmap[species] not in dict :
            dict[fishmap[species]] = []
        if weight != 'NA':
            dict[fishmap[species]].append(float(weight))
    return dict

#==========================================================
def main():
    '''
    The function of main() is to call the function (fish_dict_from_file()) to
    get the dictionary of fish names and weight, and prints the report of the
    fish type, the name, and the mean weight of the fish.
    '''
    
    fish_dict = fish_dict_from_file('fishcatch.dat')
    print(str('#').rjust(4) + ' ' + str('NAME').ljust(10) + ' ' + str('MEAN WT').rjust(10))
    for key in sorted(fish_dict.keys()):
        print ((str(len(fish_dict[key])).rjust(4)) + ' ' + key.ljust(10) + (str(round(sum(fish_dict[key]) /len(fish_dict[key]),1)) + 'g').rjust(11))

if __name__ == '__main__':
    main()
