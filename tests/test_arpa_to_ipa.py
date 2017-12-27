import csv
import unittest

import os

import logging

from arpa2ipa import arpa_to_ipa

logger = logging.getLogger(__name__)

class TestArpaToIPA(unittest.TestCase):

    def test_arpa_to_ipa_func(self):

        path = os.path.join(os.path.join(os.path.dirname(__file__), 'datasets'), 'dataset.csv')

        with open(path) as f:
            csv_reader = csv.reader(f)
            for word, arpa_str in csv_reader:
                logger.info('{} {}'.format(word, arpa_str))
                ipa_str = arpa_to_ipa(arpa_str)
                logger.info('--> {}'.format(ipa_str))




if __name__ == '__main__':
    unittest.main()
