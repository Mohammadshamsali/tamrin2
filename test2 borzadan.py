import random
SUITS =['clubs','Dimonds','Hearts','Spades']
Rank =['2','3','4','5','6','7','8','9','10']
deck=[]
b=0
for i in Rank:
    for a in SUITS:
        deck.append(i+a)
        b+=1


n = len(deck)
for i in range(n):
    r = random.randrange(0, i + 1)
    temp = deck[r]
    deck[r]=deck[i]
    deck[i]=temp
print(deck)