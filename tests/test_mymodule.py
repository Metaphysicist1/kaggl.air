import unittest
from pathlib import Path
from kaggl_air import Kaggle_air


class TestMyClass(unittest.TestCase):
    def setUp(self):
        self.downloader = Kaggle_air("TestDownloader")

    def test_initialization(self):
        self.assertEqual(self.downloader.name, "TestDownloader")
        self.assertEqual(
            self.downloader.default_destination, 
            str(Path('~/Downloads').expanduser())
        )

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main() 