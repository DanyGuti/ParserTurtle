import turtle
import re
NUM = r'(?P<NUM>[1-9])'
FORWARD = r'(?P<FORWARD>md)'
BACKWARD = r'(?P<BACKWARD>ma)'
LEFT = r'(?P<LEFT>mi)'
RIGHT = r'(?P<RIGHT>mr)'
UP = r'(?P<UP>lr)'
DOWN = r'(?P<DOWN>br)'
CHANGE = r'(?P<CHANGE>cc)'
COLOR = r'(?P<COLOR>(azul|verde|rojo|naranja|morado|amarillo|cafe|cian))'
CLEAR = r'(?P<CLEAR>clear)'
RESET = r'(?P<RESET>ct)'
SPACE = r'(?P<SPACE>\s)'
REPEAT = r'(?P<REPEAT>repetir)'
OPEN = r'(?P<OPEN>\[)'
CLOSE = r'(?P<CLOSE>\])'
STOP = r'(?P<STOP>0)'
# Dictionary with available colors
colors = {'azul': 'blue',
          'rojo': 'red',
          'verde': 'green',
          'naranja': 'orange',
          'morado': 'purple',
          'amarillo': 'yellow',
          'cafe': 'brown',
          'cian': 'cyan'
          }
window, skk = turtle.Screen(), turtle.Turtle()

window.title("Robot para ninios")
window.addshape("icons8-pixel-64.gif")
window.bgcolor(0.60160, 0, 0.99220)
window.screensize(1000, 1000)
skk.pensize(9)
skk.shape("icons8-pixel-64.gif")
skk.speed("slowest")
file = open('testCases.txt', 'r')

# Join lexems to form Lexic
master = re.compile('|'.join((NUM, FORWARD, BACKWARD, LEFT, RIGHT, UP, DOWN, CHANGE, COLOR, CLEAR, RESET, REPEAT, SPACE, STOP, OPEN, CLOSE)))
# Globals as pointers out of bounds and to repeat loop
i, j = 0, 0
listTokens = []

# askInput() Receives every input, stores every token if exists in lexic
# even if there are [ or spaces in between
def askInput():
    global i, j, master, userInput, loopList, listTokens, file
    while True:
        userInput = file.readline()
        userInput = "".join(userInput.split())
        listTokens = [m.group() for m in master.finditer(userInput)]
        loopList = listTokens
        i = 0
        # Condition that applies when there's an empty list 
        # as not a valid command or when one element in list
        # and it's not a command of just one token
        if(not listTokens or (len(listTokens) - 1 == 0 and not(
                    (re.match(CLEAR, listTokens[i]) or
                    (re.match(RESET, listTokens[i]) or
                    (re.match(STOP, listTokens[i]) or
                    (re.match(UP, listTokens[i]) or
                    (re.match(DOWN, listTokens[i]))))))))):
            print("Comando no valido, escribelo nuevamente...")
            askInput()
        if(listTokens[0] == "0" or not(listTokens)): # If empty list or "0" in index 0
            break
        else:
            command() # Start every possibility, if repeat, then
                      # ] will come at last index if j < 0 
                      # ask for input again then
            if(listTokens[-1] == "]"):
                listTokens = []
                askInput()
            if(i == 1 and j < 0):
                print("Escribe tus instrucciones nuevamente...")
                askInput()
            break
# Loop to get the parse after '[' is found
# Start the counter of j if found a NUM
def loop():
    global i, j, loopList, listTokens
    listTokens = loopList # LoopList to initialize every time if j >= 0
    if (re.match(NUM, listTokens[i])):
        checkNum()
    if(re.match(NUM,listTokens[i])):
        j = int(listTokens[i]) # Catch repeat num
    else: # When returning after every call, set i to 1
        i = 1
        for x in range(len(listTokens)):
            if(re.match(REPEAT, listTokens[x])):
                i = x + 1
                break
            i = 1
    j-=1
    if(j < 0): # Repeat has ended
        i = len(listTokens)-1
        if(re.match(REPEAT, listTokens[0]) and
           not(re.match(NUM, listTokens[1]))):
            return "0"
        print("Tu comando 'repetir' termino....")
        return "0"
    i+=1
    if(listTokens[i] == "["): # Repeat command until ']'
        i+=1
        listTokens = listTokens[i:] # Parse the list of tokens from <command> to <]>
        i = 0 # After parse, just set i to 0 and call command to match tokens
        command()
        return "0" if listTokens[i] == "]" else print("Se esperaba ']'")
    
# Command
# FW, BW, NUM, LEFT, RIGHT, UP, DOWN, CAMBIAR, COLOR, CLEAR, RESET
def command():
    global i, listTokens, loopList, listTokens
    # Condition to set new list for tokens 
    # only if two pointers set to max and less than 0
    if(i > len(listTokens) - 1 and j <= 0):
        listTokens = []
        print("Terminaron los comandos que has escrito...")
        askInput()
        i = 0
        if(listTokens[i] == "0"):
            return
    if(listTokens[i] == "]"): # Go to loop if ] is found and set i to 0 to check
        i = 0                 # if there's more to be done with j
        loop()
    z = re.match(master, listTokens[i]) # Match master (lexic) with every listToken
    hashFirst = z.groupdict()           # If there's a match at list[i] then make a hash_map
                                        # <REGEX, STATUS>
    if(hashFirst["FORWARD"] != None or hashFirst["BACKWARD"] != None or
        hashFirst["LEFT"] != None or hashFirst["RIGHT"] != None):
        # Check for forward
        if(hashFirst["FORWARD"] != None or hashFirst["BACKWARD"] != None):
            i+=1
            checkNum()
            if(listTokens[i-1] == hashFirst["FORWARD"]): 
                skk.forward(int(listTokens[i])*18)
            if(listTokens[i-1] == hashFirst["BACKWARD"]): 
                skk.forward(int(listTokens[i])*-18)
            i+=1
            command()
        if(hashFirst["LEFT"] != None):
            i+=1
            skk.right(270)
            command()
        if(hashFirst["RIGHT"] != None):
            i+=1
            skk.right(90)
            command()
    if(hashFirst["UP"] != None or hashFirst["DOWN"] != None):
        if(hashFirst["UP"] != None):
            i+=1
            skk.up()
            command()
        if(hashFirst["DOWN"] != None):
            i+=1
            skk.down()
            command()
    if(hashFirst["CHANGE"] != None):
        i+=1
        changeColor()
        if( i <= len(listTokens) - 1):
            skk.color(colors[listTokens[i]])
        i+=1
        command()
    if(hashFirst["CLEAR"] != None):
        skk.clear()
        listTokens = []
        skk.pensize(9)
        skk.speed("slowest")
        askInput()
        return
    if(hashFirst["RESET"] != None):
        skk.reset()
        listTokens = []
        skk.pensize(9)
        skk.speed("slowest")
        askInput()
        return
    if(hashFirst["REPEAT"] != None):
        i+=1   # Check for num and store in j
        loop()
        if(listTokens[i] == "]" or listTokens[i] == "0"):
            i = 0
            return
    if(listTokens[i] == "0" or i > len(listTokens) - 1):
        return
    if(listTokens[i] == "]" and j > 0):
        i = 0
        return
# Change color
def changeColor():
    global i
    if(re.match(CHANGE, listTokens[i-1])):
        return colors[listTokens[i]] if re.match(COLOR, listTokens[i]) else print("No tengo ese color")
# Check for number and advance
def checkNum():
    global i
    if(not(listTokens[i].isdigit()) and not(re.match(REPEAT, listTokens[i]))):
        print("Se esperaba un numero...")
    
    # if(not(listTokens[i].isdigit()) and re.match(BACKWARD, listTokens[i-1])):
    # print("Se esperaba un numero")

def main():
    askInput()
if __name__ == '__main__':
    main()