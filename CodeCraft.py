Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
 
prevNum = 0
currNum = 1
nextNum = prevNum + currNum 
fibNums = [prevNum, currNum ]
myTurtle.color('Red')
#Fibonacci Calculation
for i in range(14):
    nextNum = prevNum + currNum 
    prevNum = currNum 
    currNum = nextNum 
    fibNums.append(currNum )
 
#Draw a square
for x in fibNums:
    print(x)
    myTurtle.right(90)
    myTurtle.forward(x / 2)
