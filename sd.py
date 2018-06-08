classmates = ("audrey", "Michael", "ethan", "john", "riley")
print(classmates)

print("Nearest classmate: ")
print(classmates[0])

teachers = ("Aidan", "Rahul")
python_class = teachers + classmates
print("New Class: ")
print(python_class)

food_for_lunch = ["sandwich", "cheese", "crackers", "pretzels", "salad"]
print(food_for_lunch)

people = {"audrey" : "sandwich", "Michael" : "cheese"}
print(people)

print("What is your name?")
answer2 = raw_input()
print("What do you want for lunch?")
answer = raw_input()
food_for_lunch.append(answer)
print(answer2 + " wants "  + answer + " for lunch")
print(food_for_lunch)
