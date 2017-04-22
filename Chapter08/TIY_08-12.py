def make_sandwich(*itemList):
    print(itemList)
    print("You have ordered:")
    for item in itemList:
        print('*',item)


make_sandwich('club sandwich', 'egg sandwich', 'bar-bq club sandwich')

