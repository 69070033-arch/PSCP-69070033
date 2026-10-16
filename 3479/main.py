"""3479: Name of Card"""
keys = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']
names = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'Ace', 'Jack', 'Queen', 'King']
suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']

card = input().strip().upper()

print(names[keys.index(card[:-1])], 'of', suits['DHSC'.index(card[-1])])
