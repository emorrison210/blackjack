import random
import time

cards = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
    }

suits = ["Heart", "Diamond", "Spade", "Club"]

# bet function
def bet():
    return input("Place a bet: ")

# deal function
def deal(amount):
    count = 0
    dealt = []
    while count != amount:
        random_card = random.choice(list(cards.keys()))
        random_suit = random.choice(suits)
        result = random_card + " of " + random_suit + "s"
        dealt.append(result)
        count += 1
    return dealt

def calculate_points(card_list):
    total = 0
    for card in card_list:
        card_name = card.split(" ")[0]
        total += cards.get(card_name)
    return total
    
def determine_winner(p1_points, p2_points):
    winner = ""
    if p1_points == 21 and p2_points != 21:
        winner = "Player 1"
        
    elif p2_points == 21 and p1_points != 21:
        winner = "Player 2"
        
    elif p1_points == 21 and p2_points == 21:
        winner = "Tie"
    
    elif p1_points > 21 and p2_points > 21:
        winner = "Tie"
        
    elif p1_points > 21:
        winner = "Player 2"
    
    elif p2_points > 21:
        winner = "Player 1"
        
    return winner

def main():
    money_made = 0
    while True:
        p1_points = 0
        p2_points = 0
        p1_cards = []
        p2_cards = []
        bet = int(input("\nPlace a bet: "))
        print("\nDrawing 2 cards to player and host...\n")
        time.sleep(2) # time until next line is executed
        print("--- Your Cards ---\n")
            
        # cards get dealt
        p1_cards.extend(deal(2))
        p2_cards.extend(deal(2))
            
        # cards points get added up
        p1_points = calculate_points(p1_cards)
        p2_points = calculate_points(p2_cards)
        print(f"{p1_cards} = {p1_points} points\n")
        
        # determine if someone got 21 off first two cards         
        if determine_winner(p1_points, p2_points) == "Player 1":
            money_made += bet
            print(f"Player 1 Wins! You just won ${bet}\n{money_made}")
            continue
        elif determine_winner(p1_points, p2_points) == "Player 2":
            money_made -= bet
            print(f"Player 2 Wins! You just lost ${bet}\n{money_made}")
            continue
        elif determine_winner(p1_points, p2_points) == "Tie":
            print("Tie Game")
            continue
        
        # just shows the dealers face up card that got dealt second
        print("--- Dealer's Cards ---\n")
        print(f"Facedown and {p2_cards[1]}\n")
        
        # if no one won got 21 of the first 2 cards - draw another yes or no?
        while True:
            deal_another = input("Hit or Stand? Y/N \n")
            time.sleep(2)
            if deal_another == "y":
                p1_cards.extend(deal(1))
                p1_points = calculate_points(p1_cards)
                print(f"\n{p1_cards} = {p1_points} points\n")
                if p1_points > 21:
                    money_made -= bet
                    print(f"You went over 21 and lost. You lost ${bet}")
                    break
                else:
                    continue
            if deal_another != "y" and deal_another != "n":
                continue
            
            # dealer decides whether to take a card or not
            while p2_points <= 14:
                p2_cards.extend(deal(1))
                p2_points = calculate_points(p2_cards)
                print(f"Dealer gets handed a {p2_cards[2]}\n")
            time.sleep(2)
            print("Dealer decides to not draw another card and flips his facedown card\n")
            time.sleep(1.3)
            print(f"Dealers cards: {p2_cards} = {p2_points}\n")
            break
        
        if determine_winner(p1_points, p2_points) == "Player 1":
            money_made += bet
            print(f"Player 1 Wins! You just won ${bet}\n{money_made}")
            continue
        elif determine_winner(p1_points, p2_points) == "Player 2":
            money_made -= bet
            print(f"Player 2 Wins! You just lost ${bet}\n{money_made}")
            continue
        elif determine_winner(p1_points, p2_points) == "Tie":
            print("Tie Game")
            continue
        elif p1_points > p2_points:
            money_made += bet
            print(f"Player 1 Wins! You just won ${bet}. Earnings so far: {money_made}\n")
            continue
        elif p2_points > p1_points:
            money_made -= bet
            print(f"Player 2 Wins! You just lost ${bet}. Earnings so far: {money_made}\n")
            continue
        else:
            print("Tie Game\n")
            print(f"Earnings so far: {money_made}\n")
            continue
        
            
        
        #print("test")
        #print(f"You have made ${money_made}.")
                
            
            
            
main()
#print(deal(2))


# Testing Block
"""test = deal(2)
print(test)
print(calculate_points(test))"""

#determine_winner(22, 21)