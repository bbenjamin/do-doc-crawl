import requests
import time
import random

class Parser:
    def __init__(self):
        pass

    def extract_links(self, url, visited, starturl):
        from bs4 import BeautifulSoup
        try:
            html_content = self.fetch_url_content(url)
            soup = BeautifulSoup(html_content, 'html.parser')
        except Exception as e:
            print('could not access ' + url)
            return []
        links = []
        for link in soup.select('#block-system-main a[href^="/"]'):
            href = link.get('href')
            href = href.split('?')[0].split('#')[0]
            if href in visited:
                continue
            if href.startswith('https://drupal.org'):
                pass  # Keep as-is
            elif href.startswith('/docs') or href.startswith('/drupal-wiki'):
                href = 'https://drupal.org' + href
            else:
                continue

            if starturl not in href:
                print(starturl + ' not in ' + href)
                continue

            if href in visited:
                continue

            text = link.get_text(strip=True)
            links.append({'text': text, 'href': href})
        return links


    def fetch_url_content(self, url, timeout=30):
        time.sleep(2)
        agents = [
            'Mozilla/5.0 (iPhone; CPU iPhone OS 11_9_9; like Mac OS X) AppleWebKit/600.14 (KHTML, like Gecko)  Chrome/53.0.3179.339 Mobile Safari/536.1',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3_5; like Mac OS X) AppleWebKit/601.17 (KHTML, like Gecko)  Chrome/52.0.2737.365 Mobile Safari/535.2',
            'Mozilla/5.0 (Linux i654 ) AppleWebKit/603.33 (KHTML, like Gecko) Chrome/53.0.3463.393 Safari/601',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 10_5_3; like Mac OS X) AppleWebKit/600.29 (KHTML, like Gecko)  Chrome/51.0.2261.103 Mobile Safari/537.4',
            'Mozilla/5.0 (Linux; Android 4.4.4; GT-I9503T Build/KOT49H) AppleWebKit/533.44 (KHTML, like Gecko)  Chrome/52.0.1407.245 Mobile Safari/603.5',
            'Mozilla/5.0 (Android; Android 5.0; HTC Butterfly S 919d Build/LRX22G) AppleWebKit/533.48 (KHTML, like Gecko)  Chrome/48.0.2901.268 Mobile Safari/535.5',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 9_6_0; like Mac OS X) AppleWebKit/601.42 (KHTML, like Gecko)  Chrome/50.0.2383.137 Mobile Safari/535.2',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 8_2_6; en-US) AppleWebKit/600.26 (KHTML, like Gecko) Chrome/53.0.2087.131 Safari/601',
        ]
        try:
            # Best practice: set a timeout, use a user agent
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15'
            }

            response = requests.get(
                url,
                headers=headers,
                timeout=timeout
            )

            # Raise an exception for bad status codes
            response.raise_for_status()

            return response.text

        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
