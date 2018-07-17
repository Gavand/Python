'''
    Author: Gavin Andrews
    Date: 4/19/18
    Class: ISTA 130
    Section Leader: Sebastian Andrews
    
    Description:
    The function of this program is read and send a report of the frequent amount of emoticons in a tweet.
    '''

def load_twitter_dicts_from_file(file, emoticons_to_ids, ids_to_emoticons):
    '''
    This function reads the file ('fishcatch.dat'), makes a dictionary map
    of the species with a value, creates a an empty dictionary, and writes/returns
    a dictionary with the names and weights of the fish.
        
    file: the file to read the twitter emoticons
    emoticons_to_ids: turns emoticons into id
    ids_to_emoticons: turns id into emoticons
    '''
    file_reader = open(file, 'r')
    for line in file_reader:
        tweet = line.split()
        emote = tweet[0][1: len(tweet[0]) -1]
        body = tweet[1]
        user = tweet[2][1: len(tweet[2]) -1]
        if emote not in emoticons_to_ids:
            emoticons_to_ids[emote] = []
        emoticons_to_ids[emote].append(user)
        if user not in ids_to_emoticons:
            ids_to_emoticons[user] = []
        ids_to_emoticons[user].append(emote)
    return None

def find_most_common(emote):
    '''
    This function reads sends the emoticons how how many times.
        
    emote: the emotes to recognize
    '''
    main_key = ''
    num = 0
    for key in emote.keys():
        if int(len(emote[key])) > num:
            main_key = key
            num = len(emote[main_key])
    print (main_key.ljust(21) + 'occurs' + str(num).rjust(9) + ' times')
    return main_key


#==========================================================
def main():
    '''
    The function of main() is to call the functions of load_twitter_dicts_from_file() and find_most_common()
    and print the Emoticons and the UserIDs in dictionary.
    '''
    emoticons_to_ids = {}
    ids_to_emoticons = {}
    load_twitter_dicts_from_file('twitter_emoticons.dat', emoticons_to_ids, ids_to_emoticons)
    print('Emoticons: ' + str(len(emoticons_to_ids.keys())))
    
    print('UserIDs:   ' + str(len(ids_to_emoticons.keys())))
    print()
    
    for i in range(5):
        common = find_most_common(emoticons_to_ids)
        del emoticons_to_ids[common]

if __name__ == '__main__':
    main()
