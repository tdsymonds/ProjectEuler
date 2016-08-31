# https://projecteuler.net/problem=54
# Adapted the solution that I've used elsewhere for project eulur,
# hence the left, right and none. So left if player 1 and right
# player 2

import urllib2

def main():
    
    lines = urllib2.urlopen('https://projecteuler.net/project/resources/p054_poker.txt')

    player_one_hands_won = 0

    for line in lines:
        if line:
            line = line.strip()
            line = line.split(' ')
            
            left_hand = line[:5]
            right_hand = line[5:]

            p1 = PokerHand(left_hand)
            p2 = PokerHand(right_hand)

            if p1.betterHandThan(p2) == 'left':
                player_one_hands_won += 1

    print player_one_hands_won


class PokerHand:
    def __init__(self, hand):
        self.hand = hand
        self.result = self.getHand()

    def getCardDict(self):
        card_dict = {str(x):x for x in range(2,10)}
        card_dict['T'] = 10
        card_dict['J'] = 11
        card_dict['Q'] = 12
        card_dict['K'] = 13
        card_dict['A'] = 14
        return card_dict

    def getSortedRanks(self):
        card_dict = self.getCardDict()
        return sorted([card_dict[x[0]] for x in self.hand])

    def getCardCount(self):
        card_count = {}
        card_dict = self.getCardDict()
        for card in self.hand:
            card_rank = card_dict[card[0]]
            if card_rank in card_count:
                card_count[card_rank] += 1
            else:
                card_count[card_rank] = 1
        return card_count

    def getHand(self):
        card_dict = self.getCardDict()

        # is there a flush?
        flush = True
        first_suit = self.hand[0][1]
        for card in self.hand[1:]:
            if card[1] != first_suit:
                flush = False

        # is there a straight?
        sorted_ranks = self.getSortedRanks()
        straight = range(sorted_ranks[0], sorted_ranks[-1] + 1) == sorted_ranks

        # royal or straigh flush?
        if straight and flush:
            # just need to check the last card is an ace
            if sorted_ranks[-1] == 14:
                return 'RF'
            return 'SF'

        # for four of a kind and full house need to know card counts
        card_count = self.getCardCount()
        card_count_values = card_count.values()

        # four of a kind?
        if 4 in card_count_values:
            return '4K'
            
        # full house?
        if 3 in card_count_values and 2 in card_count_values: 
            return 'FH'

        # flush?
        if flush: 
            return 'FL'

        # straight?
        if straight: 
            return 'ST'

        # 3 of a kind
        if 3 in card_count_values: 
            return '3K'
            
        # 2 pair
        if 2 in card_count_values:
            tmp = card_count_values[:]
            tmp.remove(2)
            if 2 in tmp:
                return '2P'

        # pair
        if 2 in card_count_values:
            return '2K'

        # else high card
        return 'HK'

    def betterHandThan(self, right_poker_hand):
        """
        Returns left if this hand is better,
        right if the other hand is better
        and none if both hands are equal
        """
        left_hand_result = self.result
        right_hand_result = right_poker_hand.result

        outcome = self._leftOrRightHand(left_hand_result, right_hand_result)
        if outcome != 'equal':
            return outcome

        # hands are equal so need to determine better of 
        # two hands
        # royal flush
        if left_hand_result == 'RF':
            return 'none'

        # now need to start considering sorted ranks
        l_sorted_ranks = self.getSortedRanks()
        r_sorted_ranks = right_poker_hand.getSortedRanks()
        
        # straight or straight flush
        if left_hand_result in ['ST', 'SF']:
            # which straight is higher.
            outcome = self._leftOrRight(l_sorted_ranks[-1], r_sorted_ranks[-1])
            if outcome != 'equal':
                return outcome
            return 'none'

        # now need to start condiering card counts
        l_card_count = self.getCardCount()
        r_card_count = right_poker_hand.getCardCount()

        # full house
        if left_hand_result == 'FH':
            # highest three then highest two
            for i in xrange(3,1,-1):
                l_card_rank = self._getCardRank(l_card_count, i)
                r_card_rank = self._getCardRank(r_card_count, i)

                outcome = self._leftOrRight(l_card_rank, r_card_rank)
                if outcome != 'equal':
                    return outcome
            return 'none'

        # flush
        if left_hand_result == 'FL':
            # keep comparing high cards in descending order
            for i in xrange(1,6):
                outcome = self._leftOrRight(l_sorted_ranks[-i], r_sorted_ranks[-i])
                if outcome != 'equal':
                    return outcome
            return 'none'



        # 2 (pair), 3 or 4 of a kind
        if left_hand_result in ['2K', '3K', '4K']:
            l_card_rank = self._getCardRank(l_card_count, int(left_hand_result[0]))
            r_card_rank = self._getCardRank(r_card_count, int(left_hand_result[0])) 
            
            outcome = self._leftOrRight(l_card_rank, r_card_rank)
            if outcome != 'equal':
                return outcome

            # remove the kind and look for next highest
            l_sorted_ranks = [x for x in l_sorted_ranks if x != l_card_rank]
            r_sorted_ranks = [x for x in r_sorted_ranks if x != r_card_rank]

            for i in xrange(1, len(l_sorted_ranks)+1):
                outcome = self._leftOrRight(l_sorted_ranks[-i], r_sorted_ranks[-i])
                if outcome != 'equal':
                    return outcome
            return 'none'

        # 2 pair
        if left_hand_result == '2P':
            # need to extract both pairs
            l_pair1_rank = self._getCardRank(l_card_count, 2)
            del l_card_count[l_pair1_rank]
            l_pair2_rank = self._getCardRank(l_card_count, 2)
            del l_card_count[l_pair2_rank]

            r_pair1_rank = self._getCardRank(r_card_count, 2)
            del r_card_count[r_pair1_rank]
            r_pair2_rank = self._getCardRank(r_card_count, 2)
            del r_card_count[r_pair2_rank]

            # sort the pairs into lists
            l_sorted_pairs = sorted([l_pair1_rank, l_pair2_rank])
            r_sorted_pairs = sorted([r_pair1_rank, r_pair2_rank])

            for i in xrange(1, len(l_sorted_pairs)+1):
                outcome = self._leftOrRight(l_sorted_pairs[-i], r_sorted_pairs[-i])
                if outcome != 'equal':
                    return outcome

            # the pairs are both equal, so now high card
            outcome = self._leftOrRight(l_card_count.iterkeys().next(), r_card_count.iterkeys().next())
            if outcome != 'equal':
                return outcome
            return 'none'


        # high card
        for i in xrange(1, len(l_sorted_ranks)+1):
            outcome = self._leftOrRight(l_sorted_ranks[-i], r_sorted_ranks[-i])
            if outcome != 'equal':
                return outcome

        return 'none'

    def _getCardRank(self, card_count, index):
        return card_count.keys()[card_count.values().index(index)]

    def _leftOrRight(self, left_value, right_value):
        if left_value == right_value:
            return 'equal'
        if left_value > right_value:
            return 'left'
        if left_value < right_value:
            return 'right'

    def _leftOrRightHand(self, left_hand_result, right_hand_result):
        hands = {
            'RF': 9,
            'SF': 8,
            '4K': 7,
            'FH': 6,
            'FL': 5,
            'ST': 4,
            '3K': 3,
            '2P': 2,
            '2K': 1,
            'HK': 0
        }

        left = hands[left_hand_result]
        right = hands[right_hand_result]

        return self._leftOrRight(left, right)
        

if __name__ == '__main__':
    main() 