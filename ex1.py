# -*- coding: utf-8 -*-

print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print('Yay! Printing')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')
print('''I'm going to do this in python 3 just for
funsies.''')
print("I could have code like this.") # with a comment here.
#print("This won't run.")
print("This will run.")
print("Hi there #!")

print("I will now count my chickens:")
print("Hens", 25 + 30 /6)
print("Roosters", 100 - 25 *3 % 4)

print("Now I will count the eggs:")

print("Is it true that 3 +2 < 5-7?")

print(3+2<5-7)
print("What is 3+2?", 3+2)
print("What is 5-7?", 5-7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less than or equal?", 5 <= -2)


cars = 100
space_in_a_car = 4.0
drivers =30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be" , cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car." )

my_name = 'Zed A. Shaw'
my_age = 35 # he's old
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair" % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (
my_age, my_height, my_weight, my_age + my_height + my_weight))



# Python format characters

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

print("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
 


print("Mary had a little lamb.")
print("It's fleece was white as %s" % 'snow')
print("And everywhere that Mary went.")
print("." *10 )  # What'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print( end1 + end2 + end3 + end4 + end5 + end6,
 end7 + end8 + end9 + end10 + end11 + end12)


formatter = "%r %r %r %r"
print(formatter % (1,2,3,4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, True, False))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % ( 
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))

# Here's some new strange stuff, remember type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days:", days )
print("Here are the months:", months)

print( """
There's something going on here.
With these three double-quotes.
We'll be able to type as we like.
Even 4 lines if we want, or 5, or 6.
""")

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\nona line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnio\n\t* Grass
"""

print( tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)




print("How old are you?")
age = input() 
print("How tall are you?")
height = input()
print("How much do you weigh?")
weight = input() 

print("So, you're %r old, %r tall and %r heavy." % (
age, height, weight))


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
