import Google_scraper
import unittest

class Testtext_decode(unittest.TestCase):
    def test_text_decode(self):
        self.assertEqual(Google_scraper.text_decode('<body>Hello there i m here</body>'), "Hello there i m here")

    def test_text_decode1(self):
        self.assertEqual(Google_scraper.text_decode('<body background="blue>Hello there i m here<h1> title</h2></body>'), "Hello there i m here title")

    def test_text_decode2(self):
        self.assertEqual(Google_scraper.text_decode('<body>Hello there i m here\n</body>'), "Hello there i m here")

if __name__ == '_main_':
    unittest.main()