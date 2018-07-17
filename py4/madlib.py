'''
    Author: Gavin Andrews
    Date: 4/5/18
     
    Description:
    The main function of this program is to read a file from the user,
    which contains a Mad Lib story, replaces the corresponding speech labels
    (PLURAL NOUN, VERB PAST, VERB, NOUN, ADJECTIVE) with the words from
    the user, sends the new version to a new file, prints the new file version
    and prints a report of the counts and percentages on grammar and punctuation.
    '''

def print_report(file):
    '''
    This function takes a file and sends an accurate report based
    on the total number of vowels, total number of consonants,
    total number of white spaces, total number of punctuation
    characters, total number of characters, percent of vowels,
    percent of consonants, percent of white spaces, and percent
    of punctuation characters in the file.
    
    file: a Mad Lib template file from the user (called in main())
    '''

    vowel = 'aeiou'
    consonant = 'bcdfghjklmnpqrstvwxyz'
    
    count = 0
    vowel_count = 0
    consonant_count = 0
    whitespace_count = 0
    punct_count = 0

    file_read = open(file, 'r')

    for line in file_read:
        for char in line.lower():
            count += 1
            if char in vowel:
                vowel_count += 1
            elif char in consonant:
                consonant_count += 1
            elif char.isspace():
                whitespace_count += 1
            else:
                punct_count += 1
    
    total_count = vowel_count + consonant_count + whitespace_count + punct_count
    
    file_read.close()

    title = '\n-------' + file + '------'
    title_len = len(title)

    print(title)
    print(str('Vowels:').ljust(20) + str(vowel_count).rjust(5))
    print(str('Consonants:').ljust(20) + str(consonant_count).rjust(5))
    print(str('Whitespace:').ljust(20) + str(whitespace_count).rjust(5))
    print(str('Punctuation:').ljust(20) + str(punct_count).rjust(5))
    print('-------------------------')
    print(str('Total:').ljust(20) + str(count).rjust(5) + '\n')
    print(str('Percent vowels:').ljust(20) + str(round((vowel_count / total_count) * 100,1)).rjust(5))
    print(str('Percent consonants:').ljust(20) + str(round((consonant_count / count) * 100,1)).rjust(5))
    print(str('Percent spaces:').ljust(20) + str(round((whitespace_count / count) * 100,1)).rjust(5))
    print(str('Percent punctuation:').ljust(20) + str(round((punct_count / count) * 100,1)).rjust(5))
    print('=========================\n')

def replace_parts_of_speech(line, speech):
    '''
    This function asks the user for a word that corresponds to the
    correct speech label, replaces the speech label with the word,
    and returns the version with the words.
    
    line: a string that represents a line the file
    speech: the speech labels that will be replaced by the user's words
    '''
    
    line_i = line.find(speech)
    speech_len = len(speech)
    while line_i != -1:
        line = line.replace(speech, input('Enter '+ speech.lower() + ': '), 1)
        line_i = line.find(speech)
    return line

def complete_mad_lib(file):
    '''
    This function reads the file that is inputted by the user,
    index the file line by line, calls the replace_parts_of_speeech()
    function to replace the labels with inputted words, and writes
    the madlib story to a new file.

    file: a Mad Lib template file from the user (called in main())
    '''

    newfile = 'MAD_' + file

    file_read = open(file, 'r')
    file_write = open(newfile, 'w')

    speech_array = ['PLURAL NOUN', 'VERB PAST', 'VERB', 'NOUN', 'ADJECTIVE']
    for line in file_read:
        for i in range(len(speech_array)):
            word = replace_parts_of_speech(line, speech_array[i])
            line = word
        file_write.write(word)

    file_read.close()
    file_write.close()

#==========================================================
def main():
    '''
    The main() function asks the user to enter the name of a template
    file and calls the first and third function to report the count
    and to write the Mad Lib story.
    '''
    
    enter = input('Enter file name: ')
    print_report(enter)
    complete_mad_lib(enter)

if __name__ == '__main__':
    main()
