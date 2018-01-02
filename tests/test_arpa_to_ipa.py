import logging
import os
import unittest

import pandas as pd

from arpa2ipa import arpa_to_ipa

logger = logging.getLogger(__name__)

class TestArpaToIPA(unittest.TestCase):

    def test_arpa_to_ipa_func(self):

        path = os.path.join(os.path.join(os.path.dirname(__file__), 'datasets'), 'dataset.csv')

        df = pd.read_csv(path, encoding='utf-8')


        for _, (word, arpa_str, expected_ipa_str) in df.iterrows():
            logger.info('{} {} {}'.format(word, arpa_str, expected_ipa_str))
            ipa_str = arpa_to_ipa(arpa_str)
            logger.info('--> {}'.format(ipa_str))
            self.assertEqual(expected_ipa_str, ipa_str)




if __name__ == '__main__':
    unittest.main()
