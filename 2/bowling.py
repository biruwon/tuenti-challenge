import unittest


def calculate_score(rolls_score):
    game_score = [0]
    roll = 0

    for frame in range(10):

        if rolls_score[roll] == 10:
            game_score.append(rolls_score[roll] + rolls_score[roll + 1] + rolls_score[roll + 2] + game_score[frame])
            roll += 1

        elif (rolls_score[roll] + rolls_score[roll + 1]) == 10:
            game_score.append(rolls_score[roll] + rolls_score[roll + 1] + rolls_score[roll + 2] + game_score[frame])
            roll += 2

        else:
            game_score.append(rolls_score[roll] + rolls_score[roll + 1] + game_score[frame])
            roll += 2

    game_score.pop(0)

    return game_score


testInput = open('testInput.txt')
output = open('output.txt', 'w')

lines = testInput.readlines()
cases = int(lines[0])

for i in range(1, cases+1):
    rolls_score = list(map(int, (lines[2*i].split())))
    game_score = calculate_score(rolls_score)
    output.write('Case #{}: {}\n'.format(i, " ".join(map(str, game_score))))


class BowlingTestCase(unittest.TestCase):

    def test_player_score_no_strikes_or_spares(self):
        self.assertEqual(
            calculate_score([5, 4, 1, 3, 0, 7, 4, 5, 3, 0, 2, 5, 2, 4, 5, 0, 7, 1, 4, 4]),
            [9, 13, 20, 29, 32, 39, 45, 50, 58, 66]
        )

    def test_player_score_a_strike(self):
        self.assertEqual(
            calculate_score([9, 0, 4, 0, 8, 0, 4, 5, 7, 0, 10, 4, 1, 7, 1, 6, 3, 5, 4]),
            [9, 13, 21, 30, 37, 52, 57, 65, 74, 83]
        )

    def test_player_score_a_spare_plus_strikes(self):
        self.assertEqual(
            calculate_score([10, 7, 2, 9, 1, 10, 10, 7, 1, 8, 0, 7, 0, 10, 10, 4, 2]),
            [19, 28, 48, 75, 93, 101, 109, 116, 140, 156]
        )

    def test_player_made_a_perfect_game(self):
        self.assertEqual(
            calculate_score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]),
            [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
        )


if __name__ == '__main__':
    unittest.main()
