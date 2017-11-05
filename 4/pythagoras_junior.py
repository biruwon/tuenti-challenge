import unittest


# sides length are sorted from lowest to highest for efficiency
def is_triangle_possible(a, b, c):
    is_possible = False
    if a + b > c:
        is_possible = True
    return is_possible


def calculate_triangle_perimeter(a, b, c):
    return a + b + c


def smallest_triangle_perimeter(total_sides, sides_length):
    sides_length.sort()
    perimeters = []

    for i in range(0, total_sides - 2):
        for j in range(i+1, total_sides - 1):
            a, b, c = sides_length[i], sides_length[j], sides_length[j+1]
            if is_triangle_possible(a, b, c):
                perimeter = calculate_triangle_perimeter(a, b, c)
                perimeters.append(perimeter)
                break

    if len(perimeters) >= 1:
        return min(perimeters)
    else:
        return False

testInput = open('testInput.txt')
output = open('output.txt', 'w')

lines = testInput.readlines()
cases = int(lines[0])

for i in range(1, cases+1):
    testTriangleLine = list(map(int, (lines[i].split())))
    perimeter = smallest_triangle_perimeter(testTriangleLine[0], testTriangleLine[1:])
    if not perimeter:
        output.write('Case #{}: {}\n'.format(i, 'IMPOSSIBLE'))
    else:
        output.write('Case #{}: {}\n'.format(i, perimeter))


class PythagorasJuniorTestCase(unittest.TestCase):
    def test_that_a_triangle_is_possible(self):
        self.assertEqual(is_triangle_possible(1, 13, 13), True)

    def test_that_a_triangle_is_not_possible(self):
        self.assertEqual(is_triangle_possible(1, 1, 13), False)

    def test_calculate_perimeter(self):
        self.assertEqual(calculate_triangle_perimeter(1, 13, 13), 27)

    def test_calculate_smallest_triangle_perimeter(self):
        self.assertEqual(smallest_triangle_perimeter(6, [13, 9, 1, 13, 17, 6]), 27)

    def test_calculate_smallest_triangle_perimeter_not_possible(self):
        self.assertEqual(smallest_triangle_perimeter(7, [110, 40, 10, 1, 20, 60, 3]), False)


if __name__ == '__main__':
    unittest.main()
