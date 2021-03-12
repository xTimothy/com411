print("What level of brightness is required?")
level_desired = int(input())

print("\nAdjusting brightness...\n")

for level in range(2, level_desired+1, 2):
  print("Beep's brightness level:" , "*" * level)
  print("Bop's brightness level:" , "*" * level)

print("\nAdjustments complete!")