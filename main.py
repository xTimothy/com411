<<<<<<< HEAD
#Pogram that displays a menu and allows the user to either see a nice message, calculate areas of rectangle or triangle or display a times table for a number.

print("Please choose and option from the menu:\n\n1-Nice message\n2-Area of a rectangle\n3-Area of a triange\n4-Times table")

option = int(input())

if option == 1:
  print("Today will be a good day!")
elif option == 2:
  print("Enter the length of the rectangle:")
  l = int(input())
  print("Enter the width of the rectangle:")
  w = int(input())
  area = w*l 
  print("The area of this rectangle was {}".format(area))
elif option == 3:
  print("Enter the base of the triangle:")
  base = float(input())
  print("Enter the height of the triangle:")
  height = float(input())
  area = 0.5*base*height
  print("The area of this triangle was {:.2f}".format(area))
elif option == 4:
  print("What number would you like to see times table for?")
  n = int(input())
  for i in range(1,11,1):
      print("{}x{}={}".format(n,i,n*i))
else:
  print("There is no such option. Go to specsavers!")
=======
#While loop (and also FOR loop) cand be used to have a repetition of a procedure in our code

print("How many times to print the symbol?")
x = int(input()) #x=3

#i is a conter - it keeps track of how many times we went through the loop
i = 0

while i < x: #condition for repeating the code - as long as i lower than x
  print("\u27BD" , i)
  i = i + 1 #new value of the counter is more than it used to be

print("We left the loop")
>>>>>>> c8ed661a9abae99498b5fdda633ed9428e3841c6
