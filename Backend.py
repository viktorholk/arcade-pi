#mostly lightning stuff
import RPi.GPIO as GPIO
from time import sleep
#Varaibles
winnerblinktime = .15
winnerblinktime2 = .3


def gameover(all):
    for i in range(2):
        for y in all:
            if not y == 13:
                GPIO.output(y, True)
            sleep(.05)
        for y in all:
            if not y == 13:
                GPIO.output(y, False)
            sleep(.05)
        for y in all:
            if not y == 13:
                GPIO.output(y, True)
            sleep(.05)
        for y in all:
            if not y == 13:
                GPIO.output(y, False)
            sleep(.05)


def gamewon(all, yellow):
    for i in all:
        GPIO.output(i, True)
        sleep(.1)
        GPIO.output(i, False)
    for i in yellow:
        GPIO.output(i, True)
        sleep(.1)
        GPIO.output(i, False)


def winnerblink(all):
    for i in all:
        GPIO.output(i, True)
    sleep(winnerblinktime)

    for i in all:
        GPIO.output(i, False)
    sleep(winnerblinktime)

    for i in all:
        GPIO.output(i, True)
    sleep(winnerblinktime)

    for i in all:
        GPIO.output(i, False)
    sleep(winnerblinktime)

    for i in all:
        GPIO.output(i, True)
    sleep(winnerblinktime)

    for i in all:
        GPIO.output(i, False)
    sleep(winnerblinktime)
    #blink from middle

    GPIO.output(13, True)
    sleep(winnerblinktime2)
    GPIO.output(6, True)
    GPIO.output(19, True)
    sleep(winnerblinktime2)
    GPIO.output(12, True)
    GPIO.output(26, True)
    sleep(winnerblinktime2)

    sleep(.5)


def loselife(all):
    #TURN OFF ALL LIGHTS
    for x in all:
        GPIO.output(x, False)
    #TURN ON RED
    for i in all:
        if not i == 13:
            GPIO.output(i, True)
    sleep(.5)
    #OFF AGAIn
    for x in all:
        GPIO.output(x, False)
