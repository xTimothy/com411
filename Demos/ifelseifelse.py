print("What is your name?")
n = input()
# print("Do you have a dog? (types True or False)")
# dog = input()
#bool is boolean datatype - only stores True/False


if len(n) > 9:
  print("You have a very looong name!")
  print("Your name contains {} letters.".format(len(n)))
elif len(n) > 6: 
    print("Your name is a bit long. Consider a nickname")
elif len(n) < 3: 
    print("Your name is veeery short")
else:
  print("Your name is quite okay")
print("This is the END of the program!")