players = ['charles', 'martina', 'michael', 'florence', 'eli', 'hulk', 'spider man']



print("First three players from the lists are")
print(players[:3])

print("\nThree items from the middle of the lists are")
start_point = int(len(players)/2)-1
print(players[start_point:start_point+3])

print("\nLast three players from the lists are")
print(players[-3:])