def shop():
  items = {
    "Eggs": 1.99,
    "Milk": 0.99,
    "Cereals": 2.99,
    "Steak": 4.79,
    "Beer": 2.99,
    "Sausage": 1.29,
    "Vinegar": 2.49,
    "Bread": 1.49
 }
  return items

def view_all(products ={}):
  for i in products:
    print(i)

def basket():
  basket = []
  while True:
    item = input("Enter item (or \"stop\"): ")
    if item == "stop":
      break
    else:
      basket.append(item)
  return basket


def till(basket =[]):
  shoplist = shop()
  total = 0.0
  for item in basket:
    print(shoplist[item])
    total += shoplist[item]
  return total 

def run():
  print("Welcome to Teem's shop! Please have a look around and add items you like!")
  view_all(shop())
  chosen_items = basket()
  while True:
    print("Are you ready to pay?")
    if input().lower() == "yes":
      to_pay = till(chosen_items)
      print(f"Please pay £{to_pay:.2f} by cash or card:")
      break
    else:
      chosen_items += basket()

run()