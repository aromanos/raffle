import unittest

import raffle

class Tests(unittest.TestCase):

    def test_number_of_adult_results(self):
        results = raffle.run_adults()
        self.assertEquals(len(results), len(raffle.adults))

    def test_number_of_children_results(self):
        results = raffle.run_children()
        self.assertEquals(len(results), len(raffle.children))

    def test_adult_assigned_to_jaime(self):
        number_of_iterations = 100
        for iter in range(number_of_iterations):
            results = raffle.run_adults()
            self.assertIn('Jaime', results)

    def test_adult_exclusions(self):
        number_of_iterations = 100
        for iter in range(number_of_iterations):
            results = raffle.run_adults()
            self.assertNotEquals(results['Jaime'], 'Marina')
            self.assertNotEquals(results['Jaime'], 'Jaime')

    def test_children_exclusions(self):
        number_of_iterations = 100
        for iter in range(number_of_iterations):
            results = raffle.run_children()
            self.assertNotEquals(results['Jaime & Marina'], 'Julia')
            self.assertNotEquals(results['Jaime & Marina'], 'Gonzalo')

    def test_children_ana_andres(self):
        number_of_iterations = 100
        for iter in range(number_of_iterations):
            results = raffle.run_children()
            self.assertIn('Andres & Ana', results)

if __name__ == '__main__':
    unittest.main()