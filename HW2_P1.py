
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

for suit in suits:
    for rank in ranks:
        print(rank, suit)
        


for suit in suits:
    for i in range(len(ranks)):
        print(ranks[i], suit)