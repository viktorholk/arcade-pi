#LEDGAME
import RPi.GPIO as GPIO
from time import sleep
import Backend
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO PINS
reda      =  26
redb      =  19
green     =  13
redc      =  6
redd      =  12
buttonPin =  21
lights = [reda,redb,green,redc,redd]
sc1 = 22
sc2 = 27
sc3 = 17
sc4 = 4

scorelights = [sc1,sc2,sc3,sc4]

GPIO.setup(lights[0], GPIO.OUT)
GPIO.setup(lights[1], GPIO.OUT)
GPIO.setup(lights[2], GPIO.OUT)
GPIO.setup(lights[3], GPIO.OUT)
GPIO.setup(lights[4], GPIO.OUT)
GPIO.setup(scorelights[0], GPIO.OUT)
GPIO.setup(scorelights[1], GPIO.OUT)
GPIO.setup(scorelights[2], GPIO.OUT)
GPIO.setup(scorelights[3], GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Game Settings
sleepTime = .1
stepCount = 0
score = 0
lives = 3

def clear():
    os.system("clear")


class BreakIt(Exception): pass

def scoreboard():
    clear()
    print("SPEED : " + str(sleepTime))
    print("SCORE : " + str(score))
    print("LIVES : " + str(lives))


def switchled(who):
    for i in lights:
        GPIO.output(i, False)
    GPIO.output(who, True)

def game():
    try:
        scoreboard()
        while True:
            #Scoreboard
            if score >= 1:
                GPIO.output(sc1, True)
            if score >= 2:
                GPIO.output(sc2, True)
            if score >= 3:
                GPIO.output(sc3,True)
            if score >= 4:
                GPIO.output(sc4,True)
            
            
            if score >= 4:
                print("You won")
                Backend.gamewon(lights,scorelights)
                sleepTime = .1
                stepCount = 0
                score = 0
                lives = 3
            
            #Check if player is dead
            if lives <= 0:
                print("Oh dear, you died")
                Backend.gameover(lights)
                
                sleep(1)
                #RESET
                for l in scorelights:
                    GPIO.output(l,False)
                sleepTime = .1
                stepCount = 0
                score = 0
                lives = 3
                scoreboard()
                
            
            
            for i in lights:
                stepCount = i
                
                switchled(i)
                if not GPIO.input(buttonPin):
                    raise BreakIt
                sleep(sleepTime)
            for y in reversed(lights):
                stepCount = y
                
                switchled(y)
                if not GPIO.input(buttonPin):
                    raise BreakIt
                sleep(sleepTime)
    #I DONT KNOW BUT It WORKS okay :(
    except BreakIt:

        switchled(stepCount)
        sleep(1)
        #WINNER
        if stepCount == 13:
            
            global score
            score += 1
            scoreboard()
            Backend.winnerblink(lights)
            global sleepTime
            sleepTime -= .005
        #LOSER
        else:
            
            global lives
            lives -= 1
            scoreboard()
            Backend.loselife(lights)
            game()
try:
    while True:
        game()
finally:
    for l in lights:
        GPIO.output(l,False)
    for l in scorelights:
        GPIO.output(l,False)
    GPIO.cleanup()



