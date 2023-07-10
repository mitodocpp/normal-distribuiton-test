from time import sleep as wait
from random import randint as rand
bars = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
manager = 0
from os import popen as start

a = 0
b = 0
answer = "nil"

while True:
    answer = input("> ")
    if answer == "start":
        open("result.txt","w").write("")
        for i in range(0,220):
            a = rand(0, 10)
            b = rand(0, 10)
            print(str(a) + "+" + str(b) + " = " + str(a + b))
            manager = a + b
            bars[manager] += 1
            wait(0.1)
        wait(5)
        print("test ended")
        print("result:")
        for i in range(0, len(bars)):
            print("bar" + str(i) + " = " + str(bars[i]))
            start("echo " + "bar" + str(i) + "=" + str(bars[i]) + " >> result.txt")
            wait(0.1)
        print("test saved")
        start("result.txt")
