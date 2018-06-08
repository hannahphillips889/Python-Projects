import turtle
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")

prevNum = 0
currNum = 1
nextNum = prevNum + currNum
fibNums = [prevNum, currNum ]
myTurtle.color("red")
for i in range(19):
    nextNum = prevNum + currNum
    prevNum = currNum
    currNum = nextNum
    fibNums.append(currNum )
    
for x in fibNums:
    print(x)
    myTurtle.right(90)
    myTurtle.forward(x / 2)

    
