import unittest
import Google_scraper

class TestGoogle(unittest.TestCase):
    def test_Google_job_internship_scrape(self):
        self.assertEqual(Google_scraper.Google_job_internship_scrape(), "google jobs added to csv")

    def test_Google_job_newgrad_scrape(self):
        self.assertEqual(Google_scraper.Google_job_newgrad_scrape(), "google jobs added to csv")

    def test_Google_job_experienced_scrape(self):
        self.assertEqual(Google_scraper.Google_job_experienced_scrape(), "google jobs added to csv")


if __name__ == '_main_':
    unittest.main()