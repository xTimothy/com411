#Initialise an empty set
colours = set()
#Initialise non-empty set
colors = {"blue", "red", "yellow"}

#Adding elements to a set
colors.add("purple")
colours.add("red")
colours.add("black")
colours.add("green")

print(colours)
print(colors)

#Union - joining two sorted
set1 = colours.union(colors)
print(set1)

#Intersection - finding common elements
set2 = colours.intersection(colors)
print(set2)