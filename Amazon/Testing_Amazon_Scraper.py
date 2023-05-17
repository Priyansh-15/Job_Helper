import Amazon_scraper
import unittest

class TestAmazonScraper(unittest.TestCase):
    def test_Amazon_job_internship_scrape(self):
        self.assertEqual(Amazon_scraper.Amazon_job_internship_scrape(), "amazon jobs added to csv")
        
    def test_Amazon_job_newgrad_scrape(self):
        self.assertEqual(Amazon_scraper.Amazon_job_newgrad_scrape(), "amazon jobs added to csv")
        
    def test_Amazon_job_experienced_scrape(self):
        self.assertEqual(Amazon_scraper.Amazon_job_experienced_scrape(), "amazon jobs added to csv")

if __name__ == '_main_':
    unittest.main()
