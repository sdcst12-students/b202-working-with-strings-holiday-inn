#!python3
'''
##### Task 3
Split a string into 2 halves and insert a line break in the middle.  If doing so cuts a word in half, add a dash to the first line.  You will need to make use of the

len(str) function
this function returns the length of the string

(2 points)
'''
import math
def split(input):
    '''
    parameters
    str input - string to be split
    
    
    return
    str new string with line break in the middle
    '''
    z = math.floor(len(input)/2)
    mod = ""
    sstring = input[z:]
    fstring = input[0:z]
    if fstring[-1] !=" " and sstring[0] != " ":
        mod = fstring + "-\n" + sstring
    else:
        mod = fstring + "\n" + sstring

    return mod

if __name__ == "__main__":
    sentence = "There is a big balloon in the blue sky"
    assert split(sentence) == "There is a big ball-\noon in the blue sky"
    
    sentence = "I am a fat cat"
    assert split(sentence) == "I am a \nfat cat"

    sentence = "I was a fat cat"
    assert split(sentence) == "I was a\n fat cat"