print("How far are we from the cave?")
distance = int(input())

print()

for count in range(distance, 0, -1):
  print(count, "steps remaining.")

print("\nWe have reached the cave!")