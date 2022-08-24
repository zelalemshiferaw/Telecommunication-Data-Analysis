import unittest
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join("../Telecommunication-Data-Analysis/")))

from scripts import clean_telecom_dataframe

df = pd.read_csv("./tests/telecom_cleaned_data.csv")

class TestCleaTelco(unittest.TestCase):
    
    def setUp(self):
        self.clean_telecom = clean_telecom_dataframe.Telecom()
    def test_convert_to_string(self):
        self.assertEqual(self.clean_telecom.convert_to_string(df, 'Handset Type	')['Handset Type'].dtype, 'string')

    def test_convert_to_datetime(self):
        self.assertEqual(self.clean_telecom.convert_to_datetime(df, 'End')['End'].dtype, "datetime64[ns]")
    








if __name__ == "__main__":
    unittest.main()