import scrapy


class Spider2Spider(scrapy.Spider):
    '''
    Spider to collect images from unreliable sources of COVID-19 information
    '''
    name = "spider2"

    def start_requests(self):
        '''
        Request all urls in input file
        '''
        with open('../urls_MM/MMunreliableUrls3.txt', 'r') as f:
            urls = f.readlines()
        for url in urls:
            # Prepend 'http://' if the URL is missing the scheme
            if not url.startswith('http'):
                url = 'http://' + url.strip()  # Strip newline character
            try:
                yield scrapy.Request(url=url, callback=self.parse)
            except:
                print('invild url - continuing')

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
