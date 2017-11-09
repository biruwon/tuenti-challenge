import unittest


def years_to_reach_floor(last_floor_explored, number_of_shortcuts, shortcuts=None):

    shortcut_available = True if number_of_shortcuts > 0 else False

    years = 0
    current_floor = 1
    while current_floor < last_floor_explored:

        if shortcut_available and there_is_a_good_shortcut(current_floor, shortcuts):
            ending_floor, years_shortcut = get_best_good_shortcut(current_floor, shortcuts)
            current_floor = ending_floor
            years += years_shortcut
        else:
            years += current_floor
            current_floor += 1

    return years


# TODO: Duplicated code check and get
def there_is_a_good_shortcut(current_floor, shortcuts):
    for shortcut in shortcuts:
        starting_floor, ending_floor, years = shortcut[0], shortcut[1], shortcut[2]
        if (current_floor == starting_floor or (starting_floor < current_floor and ending_floor > current_floor)) and is_a_good_shortcut(starting_floor, ending_floor, years):
            return True
    return False


def get_best_good_shortcut(current_floor, shortcuts):
    for shortcut in shortcuts:
        starting_floor, ending_floor, years = shortcut[0], shortcut[1], shortcut[2]
        if (current_floor == starting_floor or (starting_floor < current_floor and ending_floor > current_floor)) and is_a_good_shortcut(starting_floor, ending_floor, years):
            return ending_floor, years


def is_a_good_shortcut(starting_floor, ending_floor, years_shortcut):
    years = 0
    for i in range(starting_floor, ending_floor):
        years += i

    return years_shortcut < years


class TheTowerCase(unittest.TestCase):
    def test_pass_one_floor_with_no_shortcut(self):
        self.assertEqual(years_to_reach_floor(2, 0), 1)

    def test_pass_multiple_floors_with_no_shortcut(self):
        self.assertEqual(years_to_reach_floor(4, 0), 6)

    def test_pass_multiple_floors_with_one_shortcut(self):
        self.assertEqual(years_to_reach_floor(4, 1, [[2, 4, 4]]), 5)

    def test_pass_multiple_floors_with_one_shortcut_which_is_larger(self):
        self.assertEqual(years_to_reach_floor(4, 1, [[2, 4, 10]]), 6)

    def test_reach_top_floor_with_multiple_shortcuts(self):
        self.assertEqual(years_to_reach_floor(4, 2, [[2, 4, 5], [1, 3, 3]]), 6)

    def test_reach_top_floor_having_to_go_down(self):
        self.assertEqual(years_to_reach_floor(9, 3, [[3, 5, 2], [4, 8, 6], [5, 8, 20]]), 19)

    def test_reach_top_floor_case_4(self):
        self.assertEqual(
            years_to_reach_floor(10, 8, [
                [1, 6, 6],
                [2, 4, 1],
                [3, 5, 5],
                [3, 6, 5],
                [7, 8, 3],
                [7, 10, 10],
                [2, 6, 2],
                [3, 5, 5]
            ]),
            16)


if __name__ == '__main__':
    unittest.main()
