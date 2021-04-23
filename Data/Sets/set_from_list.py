def observed():
  observations = []
  for x in range(7):
    observations.append(input())
  return observations 

def run():
  print("Counting observations...")
  list_of_observations = observed()
  set_of_observations = set()
  for x in range (len(list_of_observations)):
    set_of_observations.add(list_of_observations[x])
  set_of_tuples = set()
  for item in set_of_observations:
    count = 0 
    for x in range (len(list_of_observations)):
      if list_of_observations[x] == item:
        count +=1
    set_of_tuples.add((item, count))
  print(set_of_tuples)


run()