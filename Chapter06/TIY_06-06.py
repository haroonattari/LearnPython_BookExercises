favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll_list = ['jen', 'sarah', 'daniel', 'edward', 'tony', 'ivan', 'phil']

for poll_taker in poll_list:
    if poll_taker in favorite_languages.keys():
        print("Thanks {0} for taking the poll".format(poll_taker))
    else:
        print("Hi {0} you have not taken the poll yet.".format(poll_taker))

