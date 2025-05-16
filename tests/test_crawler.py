import unittest
from src.crawler.crawler import Crawler

class TestCrawler(unittest.TestCase):

    def setUp(self):
        self.crawler = Crawler(start_url='https://www.drupal.org/docs', max_depth=12)

    def test_initialization(self):
        self.assertEqual(self.crawler.start_url, 'https://www.drupal.org/docs')
        self.assertEqual(self.crawler.max_depth, 12)

    def test_crawl(self):
        result = self.crawler.crawl()
        self.assertIsInstance(result, dict)  # Ensure the result is a dictionary
        self.assertIn('https://www.drupal.org/docs', result)  # Check if the start URL is in the result

    def test_no_duplicate_links(self):
        self.crawler.crawl()
        # Assuming the crawler has a method to get all links
        all_links = self.crawler.get_all_links()
        self.assertEqual(len(all_links), len(set(all_links)))  # Ensure there are no duplicates

if __name__ == '__main__':
    unittest.main()