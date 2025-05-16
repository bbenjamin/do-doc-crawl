import unittest
from src.crawler.parser import Parser

class TestParser(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_extract_links(self):
        html_content = '''
        <div id="block-system-main">
            <a href="/link1">Link 1</a>
            <a href="/link2">Link 2</a>
            <a href="https://external.com">External Link</a>
        </div>
        '''
        expected_links = [
            {'text': 'Link 1', 'href': '/link1'},
            {'text': 'Link 2', 'href': '/link2'}
        ]
        extracted_links = self.parser.extract_links(html_content)
        self.assertEqual(extracted_links, expected_links)

    def test_no_internal_links(self):
        html_content = '''
        <div id="block-system-main">
            <a href="https://external.com">External Link</a>
        </div>
        '''
        expected_links = []
        extracted_links = self.parser.extract_links(html_content)
        self.assertEqual(extracted_links, expected_links)

    def test_empty_content(self):
        html_content = ''
        expected_links = []
        extracted_links = self.parser.extract_links(html_content)
        self.assertEqual(extracted_links, expected_links)

if __name__ == '__main__':
    unittest.main()