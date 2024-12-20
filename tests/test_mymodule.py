import unittest
from pathlib import Path
from src.kaggl_air import KaggleAir


class TestMyClass(unittest.TestCase):
    def setUp(self):
        self.downloader = KaggleAir("TestDownloader")

    def test_initialization(self):
        self.assertEqual(self.downloader.name, "TestDownloader")
        self.assertEqual(
            self.downloader.default_destination, 
            str(Path('~/Downloads').expanduser())
        )

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main() 