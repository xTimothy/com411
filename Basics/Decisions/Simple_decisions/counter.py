print("Please enter the first whole number.")
x = int(input())
print("Please enter the second whole number.")
y = int(input())
print("Please enter the third whole number.")
z = int(input())

en = 0
on = 0

if x % 2 == 0:
  en=en+1
else:
  on=on+1
if y % 2 == 0:
  en=en+1
else:
  on=on+1
if z % 2 == 0:
  en=en+1
else:
  on=on+1
print("There where {} even and {} odd numbers.".format(en,on))