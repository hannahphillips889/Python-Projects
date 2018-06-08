import turtle
myTurtle = turtle.Turtle()
myTurlte.shape("turtle")

pervNum = 0
currNum = 1
nextNum = prevNum + currNum
number_of_terms = 10
myTurtle.color("red")
for 1 in range(number_of_terms):

    print(currNum)
    for f in range(currNum - prevNum):
        myTurtle.right(360/currNum)
        myTurtle.forward(10)


    nextNum = prevNum + currNum
    prevNum = currNum
    currNum = nextNum
