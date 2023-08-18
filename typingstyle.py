import time, sys


def typewriter(text, speed=0.05):
    charcount = len(text)
    for i in range(len(text)):
        if i != charcount:
            sys.stdout.write(text[i])
            time.sleep(speed)
    print("")


def displaytext(text, borderchar="-", custom_border_length=0):
    charcount = custom_border_length
    textarray = text.split("\n")
    for x in range(len(textarray)):
        if len(textarray[x]) > charcount:
            charcount = len(textarray[x])
        textarray[x] = '| ' + textarray[x]

    output = ""; charcount += 1
    
    for x in range(len(textarray)):
        textarray[x].replace('\n', '')
        textarray[x] += ' ' * (charcount-len(textarray[x]) - 1); textarray[x] += '|';
        
    
    output += (borderchar * charcount + "\n")
    for line in textarray:
        output += (line + '\n')
    output += (borderchar * charcount + "\n")
    
    return output