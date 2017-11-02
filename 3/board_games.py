import unittest
import math


def calculate_minimum_cards(max_punctuation):

    if max_punctuation == 1:
        cards_needed = 1
    else:
        cards_needed = int(math.ceil(math.log(max_punctuation, 2)))

    return cards_needed


testInput = open('testInput.txt')
output = open('output.txt', 'w')

lines = testInput.readlines()
cases = int(lines[0])

for i in range(1, cases+1):
    max_punctuation = int(lines[i])
    cards_needed = calculate_minimum_cards(max_punctuation)
    output.write('Case #{}: {}\n'.format(i, cards_needed))


class BoardGamesCase(unittest.TestCase):
    def test_only_one_card_needed(self):
        self.assertEqual(calculate_minimum_cards(1), 1)

    def test_two_cards_needed(self):
        self.assertEqual(calculate_minimum_cards(3), 2)

    def test_three_cards_needed(self):
        self.assertEqual(calculate_minimum_cards(6), 3)


if __name__ == '__main__':
    unittest.main()
