import scrapy


class Spider3Spider(scrapy.Spider):
    '''
    Spider to collect images from reliable tweets on COVID-19 information
    '''
    name = "spider3"

    def start_requests(self):
        '''
        Request all urls in input file
        '''
        with open('../urls/TweetRealUrl.txt', 'r') as f:
            urls = f.readlines()
        for url in urls:
            # Prepend 'http://' if the URL is missing the scheme
            if not url.startswith('http'):
                url = 'http://' + url.strip()  # Strip newline character
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''
        Parse the response and extract image urls
        '''
        for img in response.css('img'):
            img_url = img.attrib.get('src')
            if img_url:
                yield {
                    'image_urls': [response.urljoin(img_url)]
                }
