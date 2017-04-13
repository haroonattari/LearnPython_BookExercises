my_friends = ['Atta Muhammad', 'Nasir Ishaque', 'Rizwan Sheikha', 'Abdul Rahim']

my_friends.insert(0, "Tasleem Raza")
my_friends.insert(2, "Owais Madani")
my_friends.append("Imran Okhai")

print("I am very sorry for this late information. We only have table for three persons")

while(len(my_friends) >= 3):
    uninvited_friend = my_friends.pop()
    print("Hi "+uninvited_friend+", I feel sorry to let you know that I can not invite you.")

for friend in my_friends:
    print("Hi "+friend+", you are still invited!")

del my_friends[0]
del my_friends[0]

print(my_friends)