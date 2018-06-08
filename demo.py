import turtle
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")

prevNum = 0
currNum = 1
nextNum = prevNum + currNum
fibNums = [prevNum + currNum ]
myTurtle.color("red")
for i in range(14):

    print(currNum)
    for f in range(currNum + prevNum):
        myTurtle.right(360/currNum)
        myTurtle.forward(10)


   
    nextNum = prevNum + currNum
    prevNum = currNum
    currNum = nextNum
