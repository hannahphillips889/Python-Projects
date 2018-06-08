
#Create a Square Class   
square = Square(100)
 
#Finding the area of your square
print(square.area())
 
#Finding the perimeter of your square
print(square.perimeter())
 
#Describing the rectangle
square.describe("A square shape")
print("Shape Type: " + square.type)
 
#Making the square 50% smaller
square.scaleSize(0.5)
 
#Print the new area of the square
print(square.area())
