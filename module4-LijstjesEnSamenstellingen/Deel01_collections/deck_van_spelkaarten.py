import random 

type= ["harten","klaveren","schoppen","ruiten"]
bijzonder= ["aas", "boer", "vrouw","heer"]
deck= ["joker","joker2"]

for x in type:
    for j in bijzonder:
        deck.append(f"{x} {j}")
    for P in range (2,10,1):
        deck.append(f"{x}{P}")

random.shuffle(deck)
for s in range(1,8):
    kaart = random.choice(deck)
    print(f"kaart {s}: {kaart}")
    deck.remove(kaart)
print (f" deck (47 kaarten): {deck}")