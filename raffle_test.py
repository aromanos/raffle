import unittest

import raffle

class Tests(unittest.TestCase):

    def test(self):
        adults_results = raffle.run_adults()
        print(adults_results)
        self.assertEquals(len(adults_results), len(raffle.adults))

if __name__ == '__main__':
    unittest.main()