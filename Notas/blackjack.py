def sum_hand(hand):
    
    a = 0
    total = 0
    
    for card in hand:
        if card in ['Q', 'J', 'K']:
            total += 10
            
        elif card == 'A':
            a += 1
        else:
            total += int(card)
            
    total += a

    while total + 11 <= 21 and a > 0:
        total += 11
        a -= 1
    
    return total
    
    

def blackjack_hand_greater_than(hand_1, hand_2):
    h1 = sum_hand(hand_1)
    h2 = sum_hand(hand_2)
    print(h1, h2)
    return h1 <= 21 and (h1 > h2 or h2 > 21)
    
blackjack_hand_greater_than(['2', 'A', '5', 'Q', '4'], ['J', '4', '3', 'A', '10'])