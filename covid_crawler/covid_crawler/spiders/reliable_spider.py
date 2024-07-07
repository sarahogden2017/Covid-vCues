import scrapy


class Spider2Spider(scrapy.Spider):
    '''
    Spider to collect images from reliable sources of COVID-19 information
    '''
    name = "reliable_spider"

    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy.pipelines.images.ImagesPipeline': 1,
        },
        'IMAGES_STORE': '../images/reliable',
        'ROBOTSTXT_OBEY': False
    }

    def start_requests(self):
        '''
        Request all urls in input file
        '''
        url_files = ['../urls_recovery/reliableUrls.txt', '../urls_coaid/NewsRealUrl.txt', '../urls_MM/MMreliableUrls3.txt']
        urls = []
        for file in url_files:
            with open(file, 'r') as f:
                urls.extend(f.readlines())
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
