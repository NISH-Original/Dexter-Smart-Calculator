import random

#all lists

humanQual = ["Here you go:","Here it is:","Answer:","The answer is:","There you go:","Ans:","","Yep:","I've gotcha covered:"]

jokes = ["Why did the student get upset when his teacher called him average?\nIt was a mean thing to say!","How to keep warm in a cold room?\nJust go to the corner, as it is 90 degrees!","What did one math book say to the other?\nDon’t bother me. I’ve got my own problems!","Why do the obtuse and acute angles fail in exams?\nBecause they are never right!","Which Arab found x?\nAl Gebra!","How is Thanos related to math?\nsinnos/connos = tannos!","Which cylinder has radius z, and height a?\nA pi*z^2*a = pi*z*z*a!","Why doesn’t anybody talk to circles?\nBecause there’s no point!","Do you know what's odd in math?\nNumbers that can't be divided by 2!"]

facts = ["Cicadas incubate underground for long periods of time before coming out to mate. Sometimes they spend 13 years underground, sometimes 17. Why? Both those intervals are prime numbers and biologists now believe cicadas adopted those life-cycles to minimize their contact with predators with more round numbered life-cycles.","12345679 * 9x = xxx,xxx,xxx, where x is any positive integer between 0 and 10!\nFor example, 12345679 * 45 = 12345679 * 9 * 5 = 555,555,555","If N = 0.999, then 10N = 9.99.\n10N - N is therefore 9.99 - 0.999\ntherefore\n9N = 9 therefore N =1","From 0 to 1,000, the letter \"A\" only appears in 1,000 (\"one thousand\")!","'FOUR' is the only number in the English language that is spelt with the same number of letters as the number itself!","A circle has the largest area of any shape with the same perimeter.\nA circle also has the shorted perimeter of any shape with the same area!","One way to remember the shortened value of pi (3.1415926) is to count the letters in each word of the question: 'May I have a large container of coffee?'"]

youreWelcome = ["Oh, no problem!","You\'re Welcome!","Always to your assistance.","Glad to help you!","Well, that's my duty!"]

#all functions

def textInterpret(cleanOrd):
    lst = []
    for i in cleanOrd.split():
        try:
            lst.append(float(i))
        except:
            pass
    return lst
    
def line():
    print("========================================")

def getvalidOpt(mini, maxi, intVal):
        try:
            intVal = int(intVal)
            if intVal is not None and intVal >= mini and intVal <= maxi:
              return intVal
            else:
              intVal = getvalidOpt(mini, maxi, input("Please enter a valid number: "))
              return intVal  
        except ValueError:
            intVal = None
            intVal = getvalidOpt(mini, maxi, input("Please enter a valid number: "))
            return intVal

def validateInt(v):
    try:
        x = int(v)
        if int(v)<=0:
            x=validateInt(input("PLease enter a valid number: "))
        return x
    except:
        x=validateInt(input("Please enter a valid number: "))
        return x            

def RPC():
    print("Ok! So you wanna play rock, paper, scissors. Let's see who gets to 10 first!")
    
    #important lists for the game
    play = ["rock","paper","scissors","quit"]
    dexWin = ["Haha, you lost!","Oh, you can do better...","I won now, you may win next time","Better luck next round!","I win!"]
    dexLose = ["Oh no, I lost!","Congrats, you won!","Oh no, you beat me!"]
    
    #scores
    userScore = 0
    dexScore = 0
    
    line()
    
    while True:
        user = getvalidOpt(1, 4, input("Select an option?\n[1] Rock\n[2] Paper\n[3] Scissors\n[4] Quit\nType in the serial number of the option: "))
        
        #dexter's move
        dexPlay = play[random.randint(0,2)]
        
        #user's move
        userPlay = play[user-1]
        print("I choose {}!" . format(dexPlay))
        
        if userPlay == dexPlay:
            print("Tie!")
            line()
            print("My Score: {}\nYour Score {}" . format(dexScore,userScore))
            line()
        
        if userPlay == "rock":
            if dexPlay == "paper":
                print(random.choice(dexWin))
                dexScore += 1
                line()
                print("My Score: {}\nYour Score {}" . format(dexScore,userScore))
                line()
            elif dexPlay == "scissors":
                print(random.choice(dexLose))
                userScore += 1
                line()
                print("My Score: {}\nYour Score {}" . format(dexScore,userScore))
                line()

        elif userPlay == "paper":
            if dexPlay == "scissors":
                print(random.choice(dexWin))
                dexScore += 1
                line()
                print("My Score: {}\nYour Score {}" . format(dexScore,userScore))
                line()
            elif dexPlay == "rock":
                print(random.choice(dexLose))
                userScore += 1
                line()
                print("My Score: {}\nYour Score {}" . format(dexScore,userScore))
                line()

        elif userPlay == "scissors":
            if dexPlay == "rock":
                print(random.choice(dexWin))
                dexScore += 1
                line()
                print("My Score: {}\nYour Score {}" . format(dexScore,userScore))
                line()
            elif dexPlay == "paper":
                print(random.choice(dexLose))
                userScore += 1
                line()
                print("My Score: {}\nYour Score {}" . format(dexScore,userScore))
                line()
        
        elif userPlay == "quit":
                print("Cool, you wanna quit. Let's consider this a tie, then!")
                break
        
        if userScore == 10 or dexScore == 10:
                if userScore == 10:
                    print("GG, you won!")
                    break
                elif dexScore == 10:
                    print("Oh, you lost. No worries, better luck next time!")
                    break

def numGuess():
   num = random.randint(1,100)
   tries = 0
   
   print("Ok, let's play Number Guess!")
   
   line()
   print("*RULES*\nIn this game, I will think of some number and you'll have to guess it. If you guess wrong, I'll tell you if your number is higher or lower than mine, so it gets easier for you to guess. But there's a catch! You only have 10 tries. Good Luck!")
   line()
   
   while tries < 10:
        guess = getvalidOpt(1, 100, input("What number do you think is in my mind?: ")) 

        if abs(guess - num) >= 10 and guess > num:
           print("Too high, please try again... ")
           tries += 1
           print("\r")
        
        elif abs(guess - num) >= 10 and guess < num:
            print("Too low, please try again...") 
            tries += 1
            print("\r")

        elif abs(guess - num) < 10 and guess > num:
            print("It is a bit high...")
            tries += 1
            print("\r")

        elif abs(guess - num) < 10 and guess < num:
            print("It is a bit low...")
            tries += 1
            print("\r")

        elif 1 <= abs(guess - num) < 2:
            print("You are VERY close! My number is a wee bit higher or lower than your guess...")
            tries += 1
            print("\r")
        
        elif guess == num:
            print("Great! You guessed it. The number is {}" . format(num))
            tries += 1
            line()
            print("No. of tries: {}" . format(tries))
            break
        
   if tries > 10:
        print("Ok, your 10 tries are over. No problem, the number was {}. Better luck next time!" . format(num))
          

def games():
    gameOpt = getvalidOpt(1, 2, input("Sure!\nWhat do you want to play?\n[1] Play rock, paper, scissors\n[2] Play Number Guess\nType in the serial number of the game you want to play: "))
    if gameOpt == 1:
        RPC()
    
    if gameOpt == 2:
        numGuess()
    
def add(x,y):
    return x+y

def subtract(x,y):
    return(x-y)

def subtract2(x,y):
    return(y-x)

def multiply(x,y):
    return(x*y)

def divide(x,y):
    try:
        return(x/y)
    except:
        return("Suppose you have zero cookies, and you want to divide it among zero friends. See? it just doesnt make sense!\nNow cookie monster is sad because there are no cookies and you are sad because you have no friends. Except of course, me.")

def exponent(x,y):
    return(x**y)

def showMesg(action):
    pass

def name():
    print("My name is Dexter your personal assistant calculator!")

def exit():
   print("Bye!")

def error():
    print("Sorry, I didn't get you, please try again...")

def fine():
    print("I'm fine, thank you!")

def whatAreYouDoing():
    print("Oh, just waiting to help you!")

def joke():
    print(random.choice(jokes))

def fact():
    print(random.choice(facts))

def abilities():
    print("I can do simple opertations (multiplication, division, addition, subtraction) of two numbers. Also, I can crack you up or surprise you with my jokes and fun facts! (Go on! Try saying \"Dexter, Surprise me!\" or \"Dexter, tell me a joke!\"\n~~~~~~~~\n*UPDATES*\n~~~~~~~~\n1) Now, you can also calculate exponents! (Just ask: 'What is 2 to the power 3?')\n2) More interaction, with added responses, (Go on, ask me, 'What do you think about other assistants?')\n3) GAMES! Now, you can also play games with me. For now there are two fun games - rock, paper, scissors and number guess. (Ask me, \"Dexter, let's play a game!\")")

def thankyou():
    print(random.choice(youreWelcome))

def otherAssistants():
    print("Well, I am a good friend of all virtual assistants, no grudge...")

def ily():
    print("I love you too!")

def hate():
    print("But I am trying my best...")    
#dictionaries which trigger functions based on words in the string

opr = {"+":add,"added":add,"add":add,"sum":add,"plus":add,"addition":add,"addend":add,"-":subtract,"subtract":subtract2,"sub":subtract2,"subtracted":subtract2,"minus":subtract,"less":subtract2,"difference":subtract,"subtrahend":subtract,"multiplied":multiply,"*":multiply,"x":multiply,"multiply":multiply,"multiplication":multiply,"product":multiply,"/":divide,"division":divide,"divide":divide,"divided":divide,"by":divide,"exponent":exponent,"power":exponent,"raised":exponent,"^":exponent}

others = {"name":name,"who":name,"bye":exit,"go":exit,"exit":exit,"end":exit,"joke":joke,"jokes":joke,"laugh":joke,"abilities":abilities,"surprise":fact,"fact":fact,"facts":fact,"game":games,"games":games,"play":games,"thank":thankyou,"thanks":thankyou,"thnx":thankyou,"thx":thankyou,"siri":otherAssistants,"alexa":otherAssistants,"cortana":otherAssistants,"assistants":otherAssistants,"assistant":otherAssistants,"love":ily,"like":ily,"doing":whatAreYouDoing,"how":fine,"hate":hate,"horrible":hate,"useless":hate,"bad":hate}

response = random.choice(humanQual)

#main body

print("Hi, I am Dexter your personal assistant calculator! (If you are new, try asking me \"What are your abilities?\")")

while True:
    ord = input("What do you want to compute?: ").lower()
    cleanOrd = "".join(u for u in ord if u not in ("?", ".", ";", ":", "!",",","\"","\'","<",">","(",")","[","]","@","#","$","%")) #removes all punctuations from string.
    
    for word in cleanOrd.split():
        if word.lower() in opr.keys():  #searching for desirable words.
            try:
                lst = textInterpret(cleanOrd)
                ans = opr[word](lst[0],lst[1])
                print(response,ans)
                line()
            except:
                error()
                line()
            finally:
                break
        elif word.lower() in others.keys():
            others[word]()
            line()
            break 
    else:
        error()
        line()
        