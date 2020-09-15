import os
import unittest
from data.dataset import Dataset

######################################   DEFINE TEST   ######################################


class DatasetTest(unittest.TestCase):
    """
    This is a class for testing different functions as needed
    """

    @classmethod
    def setUpClass(cls):
        """
        Special function that runs only once, before all the other functions run sequentially until the end.
        """
        cls.data = Dataset(transactions, blocks, ctrl_time, show_plots)

    def test_create_dataset(self):
        """
        The function to test if the length of the dataset is correct and the data type is consistent.

        Returns:
            OK if it passes the test and FAILED if it doesn't.
        """
        self.assertEqual(287653, len(self.data.create_dataset()[0]))
        self.assertEqual(144, len(self.data.create_dataset()[1]))
        self.assertEqual(type(self.data.create_dataset()[0]), type(self.data.create_dataset()[1]))


# It takes around ~90 seconds to run
if __name__ == "__main__":
    path = os.path.join(os.path.expanduser('~'), 'Downloads')
    transactions = os.path.join(path, 'txs.json')
    blocks = os.path.join(path, 'blocks.json')
    ctrl_time = False
    show_plots = False

    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)
