#!/usr/bin/python
import time

hand_names = ['High Card', 'One Pair', 'Two Pairs', 'Three of a Kind',
    'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush',
    'Royal Flush']
card_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def poker_sort(cards):
    res = []
    for card in cards:
        if card[0].isdigit():
            i = 0
            while i < len(res) and res[i][0].isdigit() and card[0] > res[i][0]:
                i += 1
        else:
            i = 0
            while i < len(res) and res[i][0].isdigit():
                i += 1
            while i < len(res):
                if card[0] == 'A':
                    i += 1
                elif card[0] == 'K':
                    if res[i][0] == 'T' or res[i][0] == 'J' or res[i][0] == 'Q': i += 1
                    else: break
                elif card[0] == 'Q':
                    if res[i][0] == 'T' or res[i][0] == 'J': i += 1
                    else: break
                elif card[0] == 'J':
                    if res[i][0] == 'T': i += 1
                    else: break
                else:
                    break
        res.insert(i,card)
    return res

def same_suit(cards):
    suit = [cards[0]]*5
    return cards == suit

def royal(cards):
    return cards == ['T', 'J', 'Q', 'K', 'A']

def straight(cards):
    for i in range(10):
        if cards == (['A']+card_values)[i:i+5]:
            return True
    return False

def x_of_a_kind(cards, x):
    values_set = list(set(cards))
    for valueS in values_set:
        count = 0
        for value in cards:
            if valueS == value: count += 1
        if count == x: return True
    return False

def full_house(cards):
    return x_of_a_kind(cards, 3) and x_of_a_kind(cards, 2)

def two_pairs(cards):
    values_set = list(set(cards))
    cantidad = 0
    for valueS in values_set:
        count = 0
        for value in cards:
            if valueS == value: count += 1
        if count == 2: cantidad += 1
    if cantidad == 2: return True
    return False

def determine_hand(cards):
    values = [card[0] for card in cards]
    suits = [card[1] for card in cards]
    
    if same_suit(suits):
        if royal(values):
            return 10
        elif straight(values):
            return 9
        else:
            return 6
    else:
        if straight(values):
            return 5
        elif x_of_a_kind(values, 4):
            return 8
        elif full_house(values):
            return 7
        elif x_of_a_kind(values, 3):
            return 4
        elif two_pairs(values):
            return 3
        elif x_of_a_kind(values, 2):
            return 2
        else:
            return 1

def high_card_winner(cards_p1, cards_p2):
    p1_won = False                    
    for i in range(len(cards_p1)-1,-1,-1):
        if card_values.index(cards_p1[i]) > card_values.index(cards_p2[i]):
            p1_won = True
            break
        if card_values.index(cards_p1[i]) < card_values.index(cards_p2[i]):
            break
    return p1_won

def one_pair_winner(cards_p1, cards_p2):
    ind_pair_p1 = 0
    ind_pair_p2 = 0

    values_set_p1 = list(set(cards_p1))
    values_set_p2 = list(set(cards_p2))
    for valueS in values_set_p1:
        count = cards_p1.count(valueS)
        if count == 2:
            ind_pair_p1 = card_values.index(valueS)
            break
    for valueS in values_set_p2:
        count = cards_p2.count(valueS)
        if count == 2:
            ind_pair_p2 = card_values.index(valueS)
            break

    if ind_pair_p1 > ind_pair_p2: return True
    if ind_pair_p1 == ind_pair_p2:
        return high_card_winner(cards_p1, cards_p2)
    return False

def two_pairs_winner(cards_p1, cards_p2):
    ind_pair1_p1 = 0
    ind_pair1_p1_set = False
    ind_pair2_p1 = 0
    
    ind_pair1_p2 = 0
    ind_pair1_p2_set = False
    ind_pair2_p2 = 0

    values_set_p1 = list(set(cards_p1))
    values_set_p2 = list(set(cards_p2))
    for valueS in values_set_p1:
        count = cards_p1.count(valueS)
        if count == 2:
            if not ind_pair1_p1_set:
                ind_pair1_p1 = card_values.index(valueS)
                ind_pair1_p1_set = True
            else:
                ind_pair2_p1 = card_values.index(valueS)
    for valueS in values_set_p2:
        count = cards_p2.count(valueS)
        if count == 2:
            if not ind_pair1_p2_set:
                ind_pair1_p2 = card_values.index(valueS)
                ind_pair1_p2_set = True
            else:
                ind_pair2_p2 = card_values.index(valueS)

    if ind_pair2_p1 > ind_pair2_p2: return True
    if ind_pair2_p1 == ind_pair2_p2:
        if ind_pair2_p1 > ind_pair2_p2: return True
        if ind_pair2_p1 == ind_pair2_p2:
            return high_card_winner(cards_p1, cards_p2)
    return False

def three_of_a_kind_winner(cards_p1, cards_p2):
    ind_trio_p1 = 0
    ind_trio_p2 = 0

    values_set_p1 = list(set(cards_p1))
    values_set_p2 = list(set(cards_p2))
    for valueS in values_set_p1:
        count = cards_p1.count(valueS)
        if count == 3:
            ind_trio_p1 = card_values.index(valueS)
            break
    for valueS in values_set_p2:
        count = cards_p2.count(valueS)
        if count == 3:
            ind_trio_p2 = card_values.index(valueS)
            break

    if ind_trio_p1 > ind_trio_p2: return True
    if ind_trio_p1 == ind_trio_p2:
        return high_card_winner(cards_p1, cards_p2)
    return False

def straight_winner(cards_p1, cards_p2):
    return cards_p1[4] > cards_p2[4]

def full_house_winner(cards_p1, cards_p2):
    ind_trio_p1 = 0
    ind_trio_p2 = 0

    values_set_p1 = list(set(cards_p1))
    values_set_p2 = list(set(cards_p2))
    for valueS in values_set_p1:
        count = cards_p1.count(valueS)
        if count == 3:
            ind_trio_p1 = card_values.index(valueS)
            break
    for valueS in values_set_p2:
        count = cards_p1.count(valueS)
        if count == 3:
            ind_trio_p2 = card_values.index(valueS)
            break

    if ind_trio_p1 > ind_trio_p2: return True
    if ind_pair_p1 == ind_pair_p2:
        return one_pair_winner(cards_p1, cards_p2)
    return False

def four_of_a_kind_winner(cards_p1, cards_p2):
    ind_four_p1 = 0
    ind_four_p2 = 0

    values_set_p1 = list(set(cards_p1))
    values_set_p2 = list(set(cards_p2))
    for valueS in values_set_p1:
        count = cards_p1.count(valueS)
        if count == 4:
            ind_four_p1 = card_values.index(valueS)
            break
    for valueS in values_set_p2:
        count = cards_p2.count(valueS)
        if count == 4:
            ind_four_p2 = card_values.index(valueS)
            break

    if ind_four_p1 > ind_four_p2: return True
    if ind_four_p1 == ind_four_p2: return one_pair_winner(cards_p1, cards_p2)
    return False

def main():
    cant_ganados_p1 = 0
    with open('p054_poker.txt','r') as f:
        for line in f:
            p1_won = False
            line_list = line.rstrip().split(" ")
            cards_p1 = poker_sort(line_list[:5])
            cards_p2 = poker_sort(line_list[5:])
            

            hand_p1 = determine_hand(cards_p1)
            hand_p2 = determine_hand(cards_p2)

            if hand_p1 > hand_p2: p1_won = True
            if hand_p1 == hand_p2:
                if hand_p1 == 1 and high_card_winner([card[0] for card in cards_p1], [card[0] for card in cards_p2]): p1_won = True
                elif hand_p1 == 2 and one_pair_winner([card[0] for card in cards_p1], [card[0] for card in cards_p2]): p1_won = True
                elif hand_p1 == 3 and two_pairs_winner([card[0] for card in cards_p1], [card[0] for card in cards_p2]): p1_won = True
                elif hand_p1 == 4 and three_of_a_kind_winner([card[0] for card in cards_p1], [card[0] for card in cards_p2]): p1_won = True
                elif hand_p1 == 5 and straight_winner([card[0] for card in cards_p1], [card[0] for card in cards_p2]): p1_won = True
                elif hand_p1 == 7 and full_house_winner([card[0] for card in cards_p1], [card[0] for card in cards_p2]): p1_won = True
                elif hand_p1 == 8 and four_of_a_kind_winner([card[0] for card in cards_p1], [card[0] for card in cards_p2]): p1_won = True
                elif hand_p1 == 9 and straight_winner([card[0] for card in cards_p1], [card[0] for card in cards_p2]): p1_won = True
            
            if p1_won: cant_ganados_p1 += 1

    print(cant_ganados_p1, "won by player 1")

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
