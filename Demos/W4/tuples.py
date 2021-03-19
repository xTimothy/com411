def student():
  print("Enter your name:")
  name = input()
  print("What is your age?")
  age = int(input())
  print("Do you have a dog?")
  dog = input()
  if dog == "yes":
    dog_bool = True
  else:
    dog_bool = False
  return name, age, dog_bool

''''
person = ("Timothy", 59, True)

print(person)

#Access element via index - just as you do with lists
print(person[1])
if person[2]:
  print("Yaaay, you have a doggo!")
else:
   print("No doggo, no fun!")

print("Which item to print?")
n = int(input())
if n < len(person):
  print(person[n-1])

#You cannot modify (mutate) a tuple!
#person[0] = "Teemo"
#print(person)

tuple2 = person + (2000, black)
print(tuple2)
print(person)
print(tuple2)
'''

print("How many students to generate?")
n = int(input())
count = 0 #Keeps track of how many repetitions we have done
all_students = []
while(count < n):
  tuplex = student()
  all_students.append(tuplex)
  count+=1
print(all_students)