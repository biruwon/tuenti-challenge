import unittest
import math


def order_enough_pizzas(slicesPerPerson):
    maxPizzaSlices = 8
    slicesNeeded = sum(slicesPerPerson)

    return math.ceil(slicesNeeded / maxPizzaSlices)


testInput = open('testInput.txt')
output = open('output.txt', 'w')

lines = testInput.readlines()
cases = int(lines[0])

for i in range(1, cases+1):
    slicesPerPerson = map(int, (lines[2*i].split()))
    pizzas = order_enough_pizzas(slicesPerPerson)
    output.write('Case #{}: {}\n'.format(i, pizzas))


class PizzaLoveTestCase(unittest.TestCase):
    def test_one_person_eats_one_pizza(self):
        self.assertEqual(order_enough_pizzas([6]), 1)

    def test_one_person_eats_more_than_one_pizza(self):
        self.assertEqual(order_enough_pizzas([17]), 3)

    def test_multiple_people_eat_one_pizza(self):
        self.assertEqual(order_enough_pizzas([1, 3, 2]), 1)

    def test_multiple_people_eat_more_than_one_pizza(self):
        self.assertEqual(order_enough_pizzas([1, 3, 4, 9, 3]), 3)


if __name__ == '__main__':
    unittest.main()
